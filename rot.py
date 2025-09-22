from transformers import pipeline, AutoTokenizer ,AutoModeForCausalLM
model_name="meta-llama/Llama/Llama-2-7b-chat"
tokenzier=AutoTokenizer.from_pretrained(model_name,device_map="auto",torch_dtype="auto")
chat=pipeline("text-generation",model=model,tokenzier=tokenzier,trust_remote_code=True)
def ask(user_prompt,history=[]):
    prompt="\n".join(history+[f"User:{user_prompt}","Assistant:"])
    our=chat(prompt,max_new_tokens=256,do_sample=True,temperature=0.7)[0]["generated_text"]
    answer=out.split("Assistant:")[-1].strip()
    history.append(f"User:{user_prompt}")
    history.append(f"Assistant:{answer}")
    return answer,history

if __name__=="main":
    history=[]
    while True:
        q=input("You:")
        if q.lower() in ("exit","quit"):break
        ans,history=ask(q,history)
        print("Bot:",ans)