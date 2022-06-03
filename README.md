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
| `/sv2/block/{waittime}` | access sv2's `/block/{waittime}` endpoint synchronously and return JSON got from SV2. | 

### SV2

| endpoint | process |
| --- | --- |
| `/health` | returns immediately. |
| `/wait/{waittime}` | waits `waittime` seconds asynchronously and returns. |
| `/block/{waittime}` | waits `waittime` seconds synchronously and returns. |

## How to start

```
docker-compose up -d
```

If you hit above command, 2 worker processes start.

## How to test

### 1. Async

If you run this command twice simultaneously, you have to wait for 10 seconds until they return.

```
curl -X POST http://localhost:3399/sv2/wait/10
```

You can run this command during running the above commands in order to confirm non-blocking.

```
curl -X GET http://localhost:3399/health
curl -X GET http://localhost:3399/sv2/health
```

### 2. Sync

If you run this command twice simultaneously, you have to wait for 10 seconds until they return.

```
curl -X POST http://localhost:3399/sv2/block/10
```

You can run this command during running the above commands, you must wait until they ends.

```
curl -X GET http://localhost:3399/health
curl -X GET http://localhost:3399/sv2/health
```
