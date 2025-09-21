#!/bin/bash

streamlit run /app/streamlit_app.py &
STREAMLIT_PID=$!

uvicorn cli_app:cli_app --host 0.0.0.0 --port 2307 --reload &
UVICORN_PID=$!

wait $STREAMLIT_PID $UVICORN_PID