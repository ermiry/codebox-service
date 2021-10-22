# Codebox API Service

### Development
```
sudo docker run \
  -it \
  --name codebox --rm \
  -p 5071:5071 --net ermiry \
  -v /home/ermiry/Documents/ermiry/Projects/codebox/codebox-service:/home/codebox \
  -e RUNTIME=development \
  -e PORT=5071 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  ermiry/codebox-service:development /bin/bash
```

## Routes

### Main

#### GET /api/codebox
**Access:** Public \
**Description:** Codebox service top level route \
**Returns:**
  - 200 on success

#### GET /api/codebox/version
**Access:** Public \
**Description:** Returns codebox service current version \
**Returns:**
  - 200 and version's json on success
