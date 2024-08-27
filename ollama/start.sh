#!/bin/sh

# Inicia el servicio de ollama en segundo plano
ollama serve &

# Espera un momento para asegurarse de que el servicio está corriendo
sleep 5

# Ahora ejecuta los comandos necesarios
ollama pull llama3.1
ollama create DataChecker -f /ollama/ModelFiles/DataChecker
ollama create TextDescriptor -f /ollama/ModelFiles/TextDescriptor

# Mantén el contenedor activo sirviendo ollama
wait
