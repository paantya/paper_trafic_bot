docker stop $(basename $(pwd))
docker rm $(basename $(pwd))
docker run --restart always -v $(pwd):/app --name $(basename $(pwd)) \
          -e PAPERPAPER__USERNAME="$PAPERPAPER__USERNAME" \
         -e PAPERPAPER__PASSWORD="$PAPERPAPER__PASSWORD" \
         -e PAPERPAPER__USER_ID="$PAPERPAPER__USER_ID" \
         -e PAPERPAPER__CHAT_ID="$PAPERPAPER__CHAT_ID" \
         -e PAPERPAPER__TELEGRAM_TOKEN="$PAPERPAPER__TELEGRAM_TOKEN" \
         python:3.6-slim /bin/sh -c "cd /app; pip3 install -r /app/requirements.txt && python3 /app/run.py 2> w.err"
