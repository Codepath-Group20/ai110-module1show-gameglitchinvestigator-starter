#!/bin/bash

echo "🚀 Starting Streamlit headless smoke test on separate port 8502..."

# Force a different port so it doesn't conflict with or kill your main debugging server
python3 -m streamlit run app.py --server.headless true --server.port 8502 &
STREAMLIT_PID=$!

# Give the server 3 seconds to spin up
sleep 3

# Hit port 8502 instead of 8501
echo "🛰️ Sending test request to local test port..."
if curl -s -I http://localhost:8502 | grep -q "200 OK"; then
    echo "✅ SUCCESS: App booted cleanly on port 8502!"
    STATUS=0
else
    echo "❌ FAILURE: App failed to respond or crashed on boot."
    STATUS=1
fi

# Clean up and kill ONLY the test process safely
echo "🧹 Cleaning up test background processes..."
if kill -0 $STREAMLIT_PID 2>/dev/null; then
    kill $STREAMLIT_PID
    echo "🧹 Test process $STREAMLIT_PID cleared safely."
else
    echo "❌ FAILURE: Streamlit test process died early."
    STATUS=1
fi

exit $STATUS
