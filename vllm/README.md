# vLLM

## Setup

Run following to host microsoft/Phi-3-mini-4k-instruct thought vLLM
```bash
HUGGINGFACEHUB_API_TOKEN=<HUGGINGFACE_TOKEN> MODEL=microsoft/Phi-3-mini-4k-instruct docker compose -f compose.yml up
```

> Note
> 
> Use your HF_TOKEN that has access to the model

## Use

```bash
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
"model": "microsoft/Phi-3-mini-4k-instruc",
"prompt": "San Francisco is a",
"max_tokens": 7,
"temperature": 0
}'
```
