
# kafka-sensor-monitor

Projeto de monitoramento de sensores com Kafka. Um produtor simula sensores de temperatura e umidade, enviando dados para o Kafka, enquanto um consumidor detecta condições de alerta.

## Tecnologias
- Python
- Kafka
- Docker Compose
- kafka-python

## Como rodar

1. Suba o Kafka:
```bash
docker-compose up -d
