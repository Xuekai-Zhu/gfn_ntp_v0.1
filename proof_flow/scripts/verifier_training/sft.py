import torch
from datasets import load_from_disk
from huggingface_hub import login
from peft import LoraConfig
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments
)
from trl import SFTTrainer

from proof_flow.src.utils import add_pad_token, get_config, get_hf_access_token

# code based on:
# https://www.philschmid.de/fine-tune-llms-in-2024-with-trl
# (from the blog of HF's tech lead)

def main():
    config = get_config(config_name="verifier_training")
    # from datasets import load_dataset
    # # Load jsonl data from disk
    # dataset = load_dataset("json", data_files="train_dataset.json", split="train")
    
    dataset = load_from_disk(config.sft.data.formatted_dataset_dir)
    train_data = dataset["train"]

    # Hugging Face model id
    model_id = config.sft.model.base_model_id
    
    # BitsAndBytesConfig int-4 config
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=config.sft.model.bnb.load_in_4bit,
        bnb_4bit_use_double_quant=config.sft.model.bnb.4bit_use_double_quant,
        bnb_4bit_quant_type=config.sft.model.bnb.4bit_quant_type,
        bnb_4bit_compute_dtype=torch.get(config.sft.model.bnb.4bit_compute_dtype),
    )
    
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        attn_implementation="flash_attention_2",
        torch_dtype=torch.bfloat16,
        quantization_config=bnb_config
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    add_pad_token(model, tokenizer)

    # LoRA config based on QLoRA paper & Sebastian Raschka experiment
    peft_config = LoraConfig(**config.sft.model.peft)

    training_args = TrainingArguments(
        **config.sft.model.training_args
    )

    # login to the hub (needed for saving the model)
    login(token=get_hf_access_token())
    
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        peft_config=peft_config,
        tokenizer=tokenizer,
    )

    # start training, the model will be automatically saved to the hub and the output directory
    trainer.train()
    
    # save model
    trainer.save_model()

    # free the memory again
    del model
    del trainer
    torch.cuda.empty_cache()
    
            