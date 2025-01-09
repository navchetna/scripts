# TGI

## Setup

Run following to host microsoft/Phi-3-mini-4k-instruct thought TGI
```bash
model=microsoft/Phi-3-mini-4k-instruct
# share a volume with the Docker container to avoid downloading weights every run
volume=$PWD/data

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data \
3.0.0   ghcr.io/huggingface/text-generation-inference:3.0.0 --model-id $model
```


## Use

```
curl localhost:8080/v1/chat/completions \
    -X POST \
    -d '{
  "model": "tgi",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is deep learning?"
    }
  ],
  "stream": true,
  "max_tokens": 20
}' \
    -H 'Content-Type: application/json'
```