mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"20h51a05a0@cmrcet.ac.in\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml