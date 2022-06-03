# FastAPI async/await Example

## Architecture

Client => SV1(port=3399) => SV2

## Endpoints

### SV1

| endpoint | process |
| --- | --- |
| `/health` | returns immediately. |
| `/sv2/health` | access sv2's `/health` endpoint and return JSON got from SV2 immediately. |
| `/sv2/wait/{waittime}` | access sv2's `/wait/{waittime}` endpoint asynchronously and return JSON got from SV2. | 

### SV2

| endpoint | process |
| --- | --- |
| `/health` | returns immediately. |
| `/wait/{waittime}` | waits `waittime` seconds asynchronously and returns. |

## How to start

```
docker-compose up -d
```

## How to test

If you run this command, you wait for 10 seconds until it returns.

```
curl -X POST http://localhost:3399/sv2/wait/10
```

You can run this command during running the above command in order to confirm non-blocking.

```
curl -X GET http://localhost:3399/health
curl -X GET http://localhost:3399/sv2/health
```
