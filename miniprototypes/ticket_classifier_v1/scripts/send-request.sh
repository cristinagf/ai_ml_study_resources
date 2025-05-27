
curl -X POST http://localhost:5050/predict \
-H "Content-Type: application/json" \
-d "{\"text\": \"Can't login to student portal\"}"

#-d '{"text": "Projector not turning on"}' 

#curl -X POST http://localhost:5050/predict -H "Content-Type: application/json"  -d "{\"text\": \"Can't login to student portal\"}"
