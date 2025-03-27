Collecting docx (from tinytroupe==0.4.0)
  Downloading docx-0.2.4.tar.gz (54 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting markdown (from tinytroupe==0.4.0)
  Downloading Markdown-3.7-py3-none-any.whl.metadata (7.0 kB)
Collecting jupyter (from tinytroupe==0.4.0)
  Downloading jupyter-1.1.1-py2.py3-none-any.whl.metadata (2.0 kB)
Requirement already satisfied: matplotlib in /home/codespace/.local/lib/python3.12/site-packages (from tinytroupe==0.4.0) (3.10.1)
Collecting pydantic (from tinytroupe==0.4.0)
  Downloading pydantic-2.10.6-py3-none-any.whl.metadata (30 kB)
Requirement already satisfied: anyio<5,>=3.5.0 in /home/codespace/.local/lib/python3.12/site-packages (from openai>=1.40->tinytroupe==0.4.0) (4.9.0)
Collecting distro<2,>=1.7.0 (from openai>=1.40->tinytroupe==0.4.0)
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Requirement already satisfied: httpx<1,>=0.23.0 in /home/codespace/.local/lib/python3.12/site-packages (from openai>=1.40->tinytroupe==0.4.0) (0.28.1)
Collecting jiter<1,>=0.4.0 (from openai>=1.40->tinytroupe==0.4.0)
  Downloading jiter-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)
Requirement already satisfied: sniffio in /home/codespace/.local/lib/python3.12/site-packages (from openai>=1.40->tinytroupe==0.4.0) (1.3.1)
Collecting tqdm>4 (from openai>=1.40->tinytroupe==0.4.0)
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Requirement already satisfied: typing-extensions<5,>=4.11 in /home/codespace/.local/lib/python3.12/site-packages (from openai>=1.40->tinytroupe==0.4.0) (4.12.2)
Collecting annotated-types>=0.6.0 (from pydantic->tinytroupe==0.4.0)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.27.2 (from pydantic->tinytroupe==0.4.0)
  Downloading pydantic_core-2.27.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)
Collecting lxml (from docx->tinytroupe==0.4.0)
  Downloading lxml-5.3.1-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Requirement already satisfied: Pillow>=2.0 in /home/codespace/.local/lib/python3.12/site-packages (from docx->tinytroupe==0.4.0) (11.1.0)
Collecting notebook (from jupyter->tinytroupe==0.4.0)
  Downloading notebook-7.3.3-py3-none-any.whl.metadata (10 kB)
Collecting jupyter-console (from jupyter->tinytroupe==0.4.0)
  Downloading jupyter_console-6.6.3-py3-none-any.whl.metadata (5.8 kB)
Requirement already satisfied: nbconvert in /home/codespace/.local/lib/python3.12/site-packages (from jupyter->tinytroupe==0.4.0) (7.16.6)
Requirement already satisfied: ipykernel in /home/codespace/.local/lib/python3.12/site-packages (from jupyter->tinytroupe==0.4.0) (6.29.5)
Collecting ipywidgets (from jupyter->tinytroupe==0.4.0)
  Downloading ipywidgets-8.1.5-py3-none-any.whl.metadata (2.3 kB)
Requirement already satisfied: jupyterlab in /home/codespace/.local/lib/python3.12/site-packages (from jupyter->tinytroupe==0.4.0) (4.3.6)
Collecting llama-index-agent-openai<0.5.0,>=0.4.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_agent_openai-0.4.6-py3-none-any.whl.metadata (727 bytes)
Collecting llama-index-cli<0.5.0,>=0.4.1 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_cli-0.4.1-py3-none-any.whl.metadata (1.5 kB)
Collecting llama-index-core<0.13.0,>=0.12.26 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_core-0.12.26-py3-none-any.whl.metadata (2.6 kB)
Collecting llama-index-embeddings-openai<0.4.0,>=0.3.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_embeddings_openai-0.3.1-py3-none-any.whl.metadata (684 bytes)
Collecting llama-index-indices-managed-llama-cloud>=0.4.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_indices_managed_llama_cloud-0.6.9-py3-none-any.whl.metadata (3.6 kB)
Collecting llama-index-llms-openai<0.4.0,>=0.3.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_llms_openai-0.3.28-py3-none-any.whl.metadata (3.3 kB)
Collecting llama-index-multi-modal-llms-openai<0.5.0,>=0.4.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_multi_modal_llms_openai-0.4.3-py3-none-any.whl.metadata (726 bytes)
Collecting llama-index-program-openai<0.4.0,>=0.3.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_program_openai-0.3.1-py3-none-any.whl.metadata (764 bytes)
Collecting llama-index-question-gen-openai<0.4.0,>=0.3.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_question_gen_openai-0.3.0-py3-none-any.whl.metadata (783 bytes)
Collecting llama-index-readers-file<0.5.0,>=0.4.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_readers_file-0.4.7-py3-none-any.whl.metadata (5.4 kB)
Collecting llama-index-readers-llama-parse>=0.4.0 (from llama-index->tinytroupe==0.4.0)
  Downloading llama_index_readers_llama_parse-0.4.0-py3-none-any.whl.metadata (3.6 kB)
Collecting nltk>3.8.1 (from llama-index->tinytroupe==0.4.0)
  Downloading nltk-3.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting llama-index-llms-azure-openai<0.4.0,>=0.3.0 (from llama-index-embeddings-azure-openai->tinytroupe==0.4.0)
  Downloading llama_index_llms_azure_openai-0.3.2-py3-none-any.whl.metadata (4.0 kB)
Collecting huggingface-hub>=0.19.0 (from huggingface-hub[inference]>=0.19.0->llama-index-embeddings-huggingface->tinytroupe==0.4.0)
  Downloading huggingface_hub-0.29.3-py3-none-any.whl.metadata (13 kB)
Collecting sentence-transformers>=2.6.1 (from llama-index-embeddings-huggingface->tinytroupe==0.4.0)
  Downloading sentence_transformers-4.0.1-py3-none-any.whl.metadata (13 kB)
Collecting aiohttp<4.0.0,>=3.9.1 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading aiohttp-3.11.14-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)
Requirement already satisfied: beautifulsoup4<5.0.0,>=4.12.3 in /home/codespace/.local/lib/python3.12/site-packages (from llama-index-readers-web->tinytroupe==0.4.0) (4.13.3)
Collecting chromedriver-autoinstaller<0.7.0,>=0.6.3 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading chromedriver_autoinstaller-0.6.4-py3-none-any.whl.metadata (2.1 kB)
Collecting html2text<2025.0.0,>=2024.2.26 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading html2text-2024.2.26.tar.gz (56 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting newspaper3k<0.3.0,>=0.2.8 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading newspaper3k-0.2.8-py3-none-any.whl.metadata (11 kB)
Collecting playwright<2.0,>=1.30 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading playwright-1.51.0-py3-none-manylinux1_x86_64.whl.metadata (3.5 kB)
Collecting selenium<5.0.0,>=4.17.2 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading selenium-4.30.0-py3-none-any.whl.metadata (7.5 kB)
Collecting spider-client<0.0.28,>=0.0.27 (from llama-index-readers-web->tinytroupe==0.4.0)
  Downloading spider-client-0.0.27.tar.gz (5.8 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: urllib3>=1.1.0 in /home/codespace/.local/lib/python3.12/site-packages (from llama-index-readers-web->tinytroupe==0.4.0) (2.3.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/codespace/.local/lib/python3.12/site-packages (from requests->tinytroupe==0.4.0) (3.4.1)
Requirement already satisfied: idna<4,>=2.5 in /home/codespace/.local/lib/python3.12/site-packages (from requests->tinytroupe==0.4.0) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in /home/codespace/.local/lib/python3.12/site-packages (from requests->tinytroupe==0.4.0) (2025.1.31)
Requirement already satisfied: contourpy>=1.0.1 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (1.3.1)
Requirement already satisfied: cycler>=0.10 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (4.56.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (1.4.8)
Requirement already satisfied: numpy>=1.23 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (2.2.4)
Requirement already satisfied: packaging>=20.0 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (24.2)
Requirement already satisfied: pyparsing>=2.3.1 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (3.2.1)
Requirement already satisfied: python-dateutil>=2.7 in /home/codespace/.local/lib/python3.12/site-packages (from matplotlib->tinytroupe==0.4.0) (2.9.0.post0)
Collecting PyJWT<3,>=1.0.0 (from PyJWT[crypto]<3,>=1.0.0->msal->tinytroupe==0.4.0)
  Downloading PyJWT-2.10.1-py3-none-any.whl.metadata (4.0 kB)
Collecting cryptography<47,>=2.5 (from msal->tinytroupe==0.4.0)
  Using cached cryptography-44.0.2-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (5.7 kB)
Requirement already satisfied: pytz>=2020.1 in /home/codespace/.local/lib/python3.12/site-packages (from pandas->tinytroupe==0.4.0) (2025.1)
Requirement already satisfied: tzdata>=2022.7 in /home/codespace/.local/lib/python3.12/site-packages (from pandas->tinytroupe==0.4.0) (2025.1)
Collecting iniconfig (from pytest->tinytroupe==0.4.0)
  Downloading iniconfig-2.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting pluggy<2,>=1.5 (from pytest->tinytroupe==0.4.0)
  Downloading pluggy-1.5.0-py3-none-any.whl.metadata (4.8 kB)
Collecting coverage>=7.5 (from coverage[toml]>=7.5->pytest-cov->tinytroupe==0.4.0)
  Downloading coverage-7.7.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (8.5 kB)
Collecting markdown-it-py>=2.2.0 (from rich->tinytroupe==0.4.0)
  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/codespace/.local/lib/python3.12/site-packages (from rich->tinytroupe==0.4.0) (2.19.1)
Collecting regex>=2022.1.18 (from tiktoken->tinytroupe==0.4.0)
  Downloading regex-2024.11.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (40 kB)
Collecting aiohappyeyeballs>=2.3.0 (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.1.2 (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading aiosignal-1.3.2-py2.py3-none-any.whl.metadata (3.8 kB)
Requirement already satisfied: attrs>=17.3.0 in /home/codespace/.local/lib/python3.12/site-packages (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0) (25.3.0)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading frozenlist-1.5.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (13 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading multidict-6.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading propcache-0.3.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<4.0.0,>=3.9.1->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading yarl-1.18.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (69 kB)
Requirement already satisfied: soupsieve>1.2 in /home/codespace/.local/lib/python3.12/site-packages (from beautifulsoup4<5.0.0,>=4.12.3->llama-index-readers-web->tinytroupe==0.4.0) (2.6)
Requirement already satisfied: cffi>=1.12 in /home/codespace/.local/lib/python3.12/site-packages (from cryptography<47,>=2.5->msal->tinytroupe==0.4.0) (1.17.1)
Requirement already satisfied: httpcore==1.* in /home/codespace/.local/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai>=1.40->tinytroupe==0.4.0) (1.0.7)
Requirement already satisfied: h11<0.15,>=0.13 in /home/codespace/.local/lib/python3.12/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai>=1.40->tinytroupe==0.4.0) (0.14.0)
Requirement already satisfied: filelock in /home/codespace/.local/lib/python3.12/site-packages (from huggingface-hub>=0.19.0->huggingface-hub[inference]>=0.19.0->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (3.13.1)
Requirement already satisfied: fsspec>=2023.5.0 in /home/codespace/.local/lib/python3.12/site-packages (from huggingface-hub>=0.19.0->huggingface-hub[inference]>=0.19.0->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (2024.6.1)
Requirement already satisfied: pyyaml>=5.1 in /home/codespace/.local/lib/python3.12/site-packages (from huggingface-hub>=0.19.0->huggingface-hub[inference]>=0.19.0->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (6.0.2)
Collecting SQLAlchemy>=1.4.49 (from SQLAlchemy[asyncio]>=1.4.49->llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading sqlalchemy-2.0.39-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.6 kB)
Collecting banks<3.0.0,>=2.0.0 (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading banks-2.0.0-py3-none-any.whl.metadata (11 kB)
Collecting dataclasses-json (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)
Collecting deprecated>=1.2.9.3 (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading Deprecated-1.2.18-py2.py3-none-any.whl.metadata (5.7 kB)
Collecting dirtyjson<2.0.0,>=1.0.8 (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading dirtyjson-1.0.8-py3-none-any.whl.metadata (11 kB)
Collecting filetype<2.0.0,>=1.2.0 (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading filetype-1.2.0-py2.py3-none-any.whl.metadata (6.5 kB)
Requirement already satisfied: nest-asyncio<2.0.0,>=1.5.8 in /home/codespace/.local/lib/python3.12/site-packages (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0) (1.6.0)
Requirement already satisfied: networkx>=3.0 in /home/codespace/.local/lib/python3.12/site-packages (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0) (3.3)
Collecting tenacity!=8.4.0,<10.0.0,>=8.2.0 (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading tenacity-9.0.0-py3-none-any.whl.metadata (1.2 kB)
Collecting typing-inspect>=0.8.0 (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)
Collecting wrapt (from llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading wrapt-1.17.2-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.4 kB)
Collecting llama-cloud<0.2.0,>=0.1.13 (from llama-index-indices-managed-llama-cloud>=0.4.0->llama-index->tinytroupe==0.4.0)
  Downloading llama_cloud-0.1.16-py3-none-any.whl.metadata (902 bytes)
Collecting azure-identity<2.0.0,>=1.15.0 (from llama-index-llms-azure-openai<0.4.0,>=0.3.0->llama-index-embeddings-azure-openai->tinytroupe==0.4.0)
  Downloading azure_identity-1.21.0-py3-none-any.whl.metadata (81 kB)
Collecting pypdf<6.0.0,>=5.1.0 (from llama-index-readers-file<0.5.0,>=0.4.0->llama-index->tinytroupe==0.4.0)
  Downloading pypdf-5.4.0-py3-none-any.whl.metadata (7.3 kB)
Collecting striprtf<0.0.27,>=0.0.26 (from llama-index-readers-file<0.5.0,>=0.4.0->llama-index->tinytroupe==0.4.0)
  Downloading striprtf-0.0.26-py3-none-any.whl.metadata (2.1 kB)
Collecting llama-parse>=0.5.0 (from llama-index-readers-llama-parse>=0.4.0->llama-index->tinytroupe==0.4.0)
  Downloading llama_parse-0.6.4.post1-py3-none-any.whl.metadata (6.9 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->tinytroupe==0.4.0)
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting cssselect>=0.9.2 (from newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading cssselect-1.3.0-py3-none-any.whl.metadata (2.6 kB)
Collecting feedparser>=5.2.1 (from newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading feedparser-6.0.11-py3-none-any.whl.metadata (2.4 kB)
Collecting tldextract>=2.0.1 (from newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading tldextract-5.1.3-py3-none-any.whl.metadata (11 kB)
Collecting feedfinder2>=0.0.4 (from newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading feedfinder2-0.0.4.tar.gz (3.3 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting jieba3k>=0.35.1 (from newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading jieba3k-0.35.1.zip (7.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.4/7.4 MB 43.4 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting tinysegmenter==0.3 (from newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading tinysegmenter-0.3.tar.gz (16 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting click (from nltk>3.8.1->llama-index->tinytroupe==0.4.0)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Requirement already satisfied: joblib in /home/codespace/.local/lib/python3.12/site-packages (from nltk>3.8.1->llama-index->tinytroupe==0.4.0) (1.4.2)
Collecting pyee<13,>=12 (from playwright<2.0,>=1.30->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading pyee-12.1.1-py3-none-any.whl.metadata (2.9 kB)
Collecting greenlet<4.0.0,>=3.1.1 (from playwright<2.0,>=1.30->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading greenlet-3.1.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Requirement already satisfied: six>=1.5 in /home/codespace/.local/lib/python3.12/site-packages (from python-dateutil>=2.7->matplotlib->tinytroupe==0.4.0) (1.17.0)
Collecting trio~=0.17 (from selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading trio-0.29.0-py3-none-any.whl.metadata (8.5 kB)
Collecting trio-websocket~=0.9 (from selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading trio_websocket-0.12.2-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: websocket-client~=1.8 in /home/codespace/.local/lib/python3.12/site-packages (from selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0) (1.8.0)
Collecting transformers<5.0.0,>=4.41.0 (from sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0)
  Downloading transformers-4.50.1-py3-none-any.whl.metadata (39 kB)
Requirement already satisfied: torch>=1.11.0 in /home/codespace/.local/lib/python3.12/site-packages (from sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (2.6.0+cpu)
Requirement already satisfied: scikit-learn in /home/codespace/.local/lib/python3.12/site-packages (from sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (1.6.1)
Requirement already satisfied: scipy in /home/codespace/.local/lib/python3.12/site-packages (from sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (1.15.2)
Requirement already satisfied: comm>=0.1.1 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (0.2.2)
Requirement already satisfied: debugpy>=1.6.5 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (1.8.13)
Requirement already satisfied: ipython>=7.23.1 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (9.0.2)
Requirement already satisfied: jupyter-client>=6.1.12 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (8.6.3)
Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (5.7.2)
Requirement already satisfied: matplotlib-inline>=0.1 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (0.1.7)
Requirement already satisfied: psutil in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (7.0.0)
Requirement already satisfied: pyzmq>=24 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (26.3.0)
Requirement already satisfied: tornado>=6.1 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (6.4.2)
Requirement already satisfied: traitlets>=5.4.0 in /home/codespace/.local/lib/python3.12/site-packages (from ipykernel->jupyter->tinytroupe==0.4.0) (5.14.3)
Collecting widgetsnbextension~=4.0.12 (from ipywidgets->jupyter->tinytroupe==0.4.0)
  Downloading widgetsnbextension-4.0.13-py3-none-any.whl.metadata (1.6 kB)
Collecting jupyterlab-widgets~=3.0.12 (from ipywidgets->jupyter->tinytroupe==0.4.0)
  Downloading jupyterlab_widgets-3.0.13-py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: prompt-toolkit>=3.0.30 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-console->jupyter->tinytroupe==0.4.0) (3.0.50)
Requirement already satisfied: async-lru>=1.0.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (2.0.5)
Requirement already satisfied: jinja2>=3.0.3 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (3.1.6)
Requirement already satisfied: jupyter-lsp>=2.0.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (2.2.5)
Requirement already satisfied: jupyter-server<3,>=2.4.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (2.15.0)
Requirement already satisfied: jupyterlab-server<3,>=2.27.1 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (2.27.3)
Requirement already satisfied: notebook-shim>=0.2 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (0.2.4)
Requirement already satisfied: setuptools>=40.8.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab->jupyter->tinytroupe==0.4.0) (76.0.0)
Requirement already satisfied: bleach!=5.0.0 in /home/codespace/.local/lib/python3.12/site-packages (from bleach[css]!=5.0.0->nbconvert->jupyter->tinytroupe==0.4.0) (6.2.0)
Requirement already satisfied: defusedxml in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (0.7.1)
Requirement already satisfied: jupyterlab-pygments in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (0.3.0)
Requirement already satisfied: markupsafe>=2.0 in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (3.0.2)
Requirement already satisfied: mistune<4,>=2.0.3 in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (3.1.2)
Requirement already satisfied: nbclient>=0.5.0 in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (0.10.2)
Requirement already satisfied: nbformat>=5.7 in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (5.10.4)
Requirement already satisfied: pandocfilters>=1.4.1 in /home/codespace/.local/lib/python3.12/site-packages (from nbconvert->jupyter->tinytroupe==0.4.0) (1.5.1)
Collecting azure-core>=1.31.0 (from azure-identity<2.0.0,>=1.15.0->llama-index-llms-azure-openai<0.4.0,>=0.3.0->llama-index-embeddings-azure-openai->tinytroupe==0.4.0)
  Downloading azure_core-1.32.0-py3-none-any.whl.metadata (39 kB)
Collecting msal-extensions>=1.2.0 (from azure-identity<2.0.0,>=1.15.0->llama-index-llms-azure-openai<0.4.0,>=0.3.0->llama-index-embeddings-azure-openai->tinytroupe==0.4.0)
  Downloading msal_extensions-1.3.1-py3-none-any.whl.metadata (7.8 kB)
Collecting griffe (from banks<3.0.0,>=2.0.0->llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading griffe-1.6.3-py3-none-any.whl.metadata (5.0 kB)
Requirement already satisfied: webencodings in /home/codespace/.local/lib/python3.12/site-packages (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert->jupyter->tinytroupe==0.4.0) (0.5.1)
Requirement already satisfied: tinycss2<1.5,>=1.1.0 in /home/codespace/.local/lib/python3.12/site-packages (from bleach[css]!=5.0.0->nbconvert->jupyter->tinytroupe==0.4.0) (1.4.0)
Requirement already satisfied: pycparser in /home/codespace/.local/lib/python3.12/site-packages (from cffi>=1.12->cryptography<47,>=2.5->msal->tinytroupe==0.4.0) (2.22)
Collecting sgmllib3k (from feedparser>=5.2.1->newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading sgmllib3k-1.0.0.tar.gz (5.8 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: decorator in /home/codespace/.local/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (5.2.1)
Requirement already satisfied: ipython-pygments-lexers in /home/codespace/.local/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (1.1.1)
Requirement already satisfied: jedi>=0.16 in /home/codespace/.local/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (0.19.2)
Requirement already satisfied: pexpect>4.3 in /home/codespace/.local/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (4.9.0)
Requirement already satisfied: stack_data in /home/codespace/.local/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (0.6.3)
Requirement already satisfied: platformdirs>=2.5 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-core!=5.0.*,>=4.12->ipykernel->jupyter->tinytroupe==0.4.0) (4.3.6)
Requirement already satisfied: argon2-cffi>=21.1 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (23.1.0)
Requirement already satisfied: jupyter-events>=0.11.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (0.12.0)
Requirement already satisfied: jupyter-server-terminals>=0.4.4 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (0.5.3)
Requirement already satisfied: overrides>=5.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (7.7.0)
Requirement already satisfied: prometheus-client>=0.9 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (0.21.1)
Requirement already satisfied: send2trash>=1.8.2 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (1.8.3)
Requirement already satisfied: terminado>=0.8.3 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (0.18.1)
Requirement already satisfied: babel>=2.10 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab-server<3,>=2.27.1->jupyterlab->jupyter->tinytroupe==0.4.0) (2.17.0)
Requirement already satisfied: json5>=0.9.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab-server<3,>=2.27.1->jupyterlab->jupyter->tinytroupe==0.4.0) (0.10.0)
Requirement already satisfied: jsonschema>=4.18.0 in /home/codespace/.local/lib/python3.12/site-packages (from jupyterlab-server<3,>=2.27.1->jupyterlab->jupyter->tinytroupe==0.4.0) (4.23.0)
Collecting llama-cloud-services>=0.6.4 (from llama-parse>=0.5.0->llama-index-readers-llama-parse>=0.4.0->llama-index->tinytroupe==0.4.0)
  Downloading llama_cloud_services-0.6.8-py3-none-any.whl.metadata (2.9 kB)
Requirement already satisfied: fastjsonschema>=2.15 in /home/codespace/.local/lib/python3.12/site-packages (from nbformat>=5.7->nbconvert->jupyter->tinytroupe==0.4.0) (2.21.1)
Requirement already satisfied: wcwidth in /home/codespace/.local/lib/python3.12/site-packages (from prompt-toolkit>=3.0.30->jupyter-console->jupyter->tinytroupe==0.4.0) (0.2.13)
Collecting requests-file>=1.4 (from tldextract>=2.0.1->newspaper3k<0.3.0,>=0.2.8->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading requests_file-2.1.0-py2.py3-none-any.whl.metadata (1.7 kB)
Requirement already satisfied: sympy==1.13.1 in /home/codespace/.local/lib/python3.12/site-packages (from torch>=1.11.0->sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /home/codespace/.local/lib/python3.12/site-packages (from sympy==1.13.1->torch>=1.11.0->sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (1.3.0)
Collecting tokenizers<0.22,>=0.21 (from transformers<5.0.0,>=4.41.0->sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0)
  Downloading tokenizers-0.21.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
Collecting safetensors>=0.4.3 (from transformers<5.0.0,>=4.41.0->sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0)
  Downloading safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.8 kB)
Collecting sortedcontainers (from trio~=0.17->selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
Collecting outcome (from trio~=0.17->selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting wsproto>=0.14 (from trio-websocket~=0.9->selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)
Collecting mypy-extensions>=0.3.0 (from typing-inspect>=0.8.0->llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)
Collecting pysocks!=1.5.7,<2.0,>=1.5.6 (from urllib3[socks]<3,>=1.26->selenium<5.0.0,>=4.17.2->llama-index-readers-web->tinytroupe==0.4.0)
  Downloading PySocks-1.7.1-py3-none-any.whl.metadata (13 kB)
Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json->llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0)
  Downloading marshmallow-3.26.1-py3-none-any.whl.metadata (7.3 kB)
Requirement already satisfied: threadpoolctl>=3.1.0 in /home/codespace/.local/lib/python3.12/site-packages (from scikit-learn->sentence-transformers>=2.6.1->llama-index-embeddings-huggingface->tinytroupe==0.4.0) (3.6.0)
Requirement already satisfied: argon2-cffi-bindings in /home/codespace/.local/lib/python3.12/site-packages (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (21.2.0)
Requirement already satisfied: parso<0.9.0,>=0.8.4 in /home/codespace/.local/lib/python3.12/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (0.8.4)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab->jupyter->tinytroupe==0.4.0) (2024.10.1)
Requirement already satisfied: referencing>=0.28.4 in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab->jupyter->tinytroupe==0.4.0) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab->jupyter->tinytroupe==0.4.0) (0.23.1)
Requirement already satisfied: python-json-logger>=2.0.4 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (3.3.0)
Requirement already satisfied: rfc3339-validator in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (0.1.4)
Requirement already satisfied: rfc3986-validator>=0.1.1 in /home/codespace/.local/lib/python3.12/site-packages (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (0.1.1)
Collecting python-dotenv<2.0.0,>=1.0.1 (from llama-cloud-services>=0.6.4->llama-parse>=0.5.0->llama-index-readers-llama-parse>=0.4.0->llama-index->tinytroupe==0.4.0)
  Downloading python_dotenv-1.1.0-py3-none-any.whl.metadata (24 kB)
Requirement already satisfied: ptyprocess>=0.5 in /home/codespace/.local/lib/python3.12/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (0.7.0)
Requirement already satisfied: colorama>=0.4 in /home/codespace/.local/lib/python3.12/site-packages (from griffe->banks<3.0.0,>=2.0.0->llama-index-core<0.13.0,>=0.12.26->llama-index->tinytroupe==0.4.0) (0.4.6)
Requirement already satisfied: executing>=1.2.0 in /home/codespace/.local/lib/python3.12/site-packages (from stack_data->ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (2.2.0)
Requirement already satisfied: asttokens>=2.1.0 in /home/codespace/.local/lib/python3.12/site-packages (from stack_data->ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (3.0.0)
Requirement already satisfied: pure-eval in /home/codespace/.local/lib/python3.12/site-packages (from stack_data->ipython>=7.23.1->ipykernel->jupyter->tinytroupe==0.4.0) (0.2.3)
Requirement already satisfied: fqdn in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (1.5.1)
Requirement already satisfied: isoduration in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (20.11.0)
Requirement already satisfied: jsonpointer>1.13 in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (3.0.0)
Requirement already satisfied: uri-template in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (1.3.0)
Requirement already satisfied: webcolors>=24.6.0 in /home/codespace/.local/lib/python3.12/site-packages (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (24.11.1)
Requirement already satisfied: arrow>=0.15.0 in /home/codespace/.local/lib/python3.12/site-packages (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (1.3.0)
Requirement already satisfied: types-python-dateutil>=2.8.10 in /home/codespace/.local/lib/python3.12/site-packages (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab->jupyter->tinytroupe==0.4.0) (2.9.0.20241206)
Downloading openai-1.68.2-py3-none-any.whl (606 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 606.1/606.1 kB 25.5 MB/s eta 0:00:00
Downloading pydantic-2.10.6-py3-none-any.whl (431 kB)
Downloading pydantic_core-2.27.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 46.8 MB/s eta 0:00:00
Downloading chevron-0.14.0-py3-none-any.whl (11 kB)
Downloading jupyter-1.1.1-py2.py3-none-any.whl (2.7 kB)
Downloading llama_index-0.12.26-py3-none-any.whl (7.0 kB)
Downloading llama_index_embeddings_azure_openai-0.3.2-py3-none-any.whl (4.4 kB)
Downloading llama_index_embeddings_huggingface-0.5.2-py3-none-any.whl (8.9 kB)
Downloading llama_index_readers_web-0.3.8-py3-none-any.whl (97 kB)
Downloading Markdown-3.7-py3-none-any.whl (106 kB)
Downloading msal-1.32.0-py3-none-any.whl (114 kB)
Downloading pypandoc-1.15-py3-none-any.whl (21 kB)
Downloading pytest-8.3.5-py3-none-any.whl (343 kB)
Downloading pytest_cov-6.0.0-py3-none-any.whl (22 kB)
Downloading rich-13.9.4-py3-none-any.whl (242 kB)
Downloading tiktoken-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 40.0 MB/s eta 0:00:00
Downloading aiohttp-3.11.14-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 39.1 MB/s eta 0:00:00
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading chromedriver_autoinstaller-0.6.4-py3-none-any.whl (7.6 kB)
Downloading coverage-7.7.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (244 kB)
Using cached cryptography-44.0.2-cp39-abi3-manylinux_2_28_x86_64.whl (4.2 MB)
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading huggingface_hub-0.29.3-py3-none-any.whl (468 kB)
Downloading jiter-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (351 kB)
Downloading llama_index_agent_openai-0.4.6-py3-none-any.whl (13 kB)
Downloading llama_index_cli-0.4.1-py3-none-any.whl (28 kB)
Downloading llama_index_core-0.12.26-py3-none-any.whl (1.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 36.4 MB/s eta 0:00:00
Downloading llama_index_embeddings_openai-0.3.1-py3-none-any.whl (6.2 kB)
Downloading llama_index_indices_managed_llama_cloud-0.6.9-py3-none-any.whl (14 kB)
Downloading llama_index_llms_azure_openai-0.3.2-py3-none-any.whl (7.3 kB)
Downloading llama_index_llms_openai-0.3.28-py3-none-any.whl (16 kB)
Downloading llama_index_multi_modal_llms_openai-0.4.3-py3-none-any.whl (5.9 kB)
Downloading llama_index_program_openai-0.3.1-py3-none-any.whl (5.3 kB)
Downloading llama_index_question_gen_openai-0.3.0-py3-none-any.whl (2.9 kB)
Downloading llama_index_readers_file-0.4.7-py3-none-any.whl (40 kB)
Downloading llama_index_readers_llama_parse-0.4.0-py3-none-any.whl (2.5 kB)
Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Downloading newspaper3k-0.2.8-py3-none-any.whl (211 kB)
Downloading lxml-5.3.1-cp312-cp312-manylinux_2_28_x86_64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 36.9 MB/s eta 0:00:00
Downloading nltk-3.9.1-py3-none-any.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 43.4 MB/s eta 0:00:00
Downloading playwright-1.51.0-py3-none-manylinux1_x86_64.whl (45.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.2/45.2 MB 49.9 MB/s eta 0:00:00
Downloading pluggy-1.5.0-py3-none-any.whl (20 kB)
Downloading PyJWT-2.10.1-py3-none-any.whl (22 kB)
Downloading regex-2024.11.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (796 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 796.9/796.9 kB 32.4 MB/s eta 0:00:00
Downloading selenium-4.30.0-py3-none-any.whl (9.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.4/9.4 MB 47.7 MB/s eta 0:00:00
Downloading sentence_transformers-4.0.1-py3-none-any.whl (340 kB)
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
Downloading iniconfig-2.1.0-py3-none-any.whl (6.0 kB)
Downloading ipywidgets-8.1.5-py3-none-any.whl (139 kB)
Downloading jupyter_console-6.6.3-py3-none-any.whl (24 kB)
Downloading notebook-7.3.3-py3-none-any.whl (13.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.1/13.1 MB 58.9 MB/s eta 0:00:00
Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Downloading aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Downloading azure_identity-1.21.0-py3-none-any.whl (189 kB)
Downloading banks-2.0.0-py3-none-any.whl (28 kB)
Downloading cssselect-1.3.0-py3-none-any.whl (18 kB)
Downloading Deprecated-1.2.18-py2.py3-none-any.whl (10.0 kB)
Downloading dirtyjson-1.0.8-py3-none-any.whl (25 kB)
Downloading feedparser-6.0.11-py3-none-any.whl (81 kB)
Downloading filetype-1.2.0-py2.py3-none-any.whl (19 kB)
Downloading frozenlist-1.5.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (283 kB)
Downloading greenlet-3.1.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (613 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 613.1/613.1 kB 25.5 MB/s eta 0:00:00
Downloading jupyterlab_widgets-3.0.13-py3-none-any.whl (214 kB)
Downloading llama_cloud-0.1.16-py3-none-any.whl (251 kB)
Downloading llama_parse-0.6.4.post1-py3-none-any.whl (4.9 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading multidict-6.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (132 kB)
Downloading propcache-0.3.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (245 kB)
Downloading pyee-12.1.1-py3-none-any.whl (15 kB)
Downloading pypdf-5.4.0-py3-none-any.whl (302 kB)
Downloading sqlalchemy-2.0.39-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 20.5 MB/s eta 0:00:00
Downloading striprtf-0.0.26-py3-none-any.whl (6.9 kB)
Downloading tenacity-9.0.0-py3-none-any.whl (28 kB)
Downloading tldextract-5.1.3-py3-none-any.whl (104 kB)
Downloading transformers-4.50.1-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 57.1 MB/s eta 0:00:00
Downloading trio-0.29.0-py3-none-any.whl (492 kB)
Downloading trio_websocket-0.12.2-py3-none-any.whl (21 kB)
Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)
Downloading widgetsnbextension-4.0.13-py3-none-any.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 44.3 MB/s eta 0:00:00
Downloading wrapt-1.17.2-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (89 kB)
Downloading yarl-1.18.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (336 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)
Downloading azure_core-1.32.0-py3-none-any.whl (198 kB)
Downloading llama_cloud_services-0.6.8-py3-none-any.whl (29 kB)
Downloading marshmallow-3.26.1-py3-none-any.whl (50 kB)
Downloading msal_extensions-1.3.1-py3-none-any.whl (20 kB)
Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)
Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)
Downloading PySocks-1.7.1-py3-none-any.whl (16 kB)
Downloading requests_file-2.1.0-py2.py3-none-any.whl (4.2 kB)
Downloading safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (471 kB)
Downloading tokenizers-0.21.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 51.3 MB/s eta 0:00:00
Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)
Downloading griffe-1.6.3-py3-none-any.whl (128 kB)
Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Downloading python_dotenv-1.1.0-py3-none-any.whl (20 kB)
Building wheels for collected packages: tinytroupe, docx, html2text, tinysegmenter, spider-client, feedfinder2, jieba3k, sgmllib3k
  Building wheel for tinytroupe (pyproject.toml) ... done
  Created wheel for tinytroupe: filename=tinytroupe-0.4.0-py3-none-any.whl size=154714 sha256=07ed34244407b7c9f1eb5866dac64c6daa9bc7ee5671819ebb08f5a426cc57b6
  Stored in directory: /tmp/pip-ephem-wheel-cache-cufdg92z/wheels/13/4e/a0/1c6c446297173eccc7cc16bff86216f767a49a1e43c259e645
  Building wheel for docx (pyproject.toml) ... done
  Created wheel for docx: filename=docx-0.2.4-py3-none-any.whl size=53931 sha256=aa519dd50f41b382147c7ba1d609c342ff19aa3f4e7b1681ef56237f24620147
  Stored in directory: /home/codespace/.cache/pip/wheels/f3/ba/dd/43ed5f165600f41deddeb1e382c56ffc1067c09ec5bd705f39
  Building wheel for html2text (pyproject.toml) ... done
  Created wheel for html2text: filename=html2text-2024.2.26-py3-none-any.whl size=33169 sha256=8cb6c81906822b7778e273a73ec79fe251a0524baf22e59088e7516089a50d9a
  Stored in directory: /home/codespace/.cache/pip/wheels/2b/01/23/578505d65e2a97d78bf1fe3fc8256ecf37572dc1df598b0eaf
  Building wheel for tinysegmenter (pyproject.toml) ... done
  Created wheel for tinysegmenter: filename=tinysegmenter-0.3-py3-none-any.whl size=13634 sha256=cc1889749ab9344837d63faad25b16cabcff581b1f57ded66d2dfe07c65ec010
  Stored in directory: /home/codespace/.cache/pip/wheels/a5/91/9f/00d66475960891a64867914273fcaf78df6cb04d905b104a2a
  Building wheel for spider-client (pyproject.toml) ... done
  Created wheel for spider-client: filename=spider_client-0.0.27-py3-none-any.whl size=6053 sha256=731dff53fed69630a65362486f0850264389cffb8e57a8bbd5eee4fbd0fa4751
  Stored in directory: /home/codespace/.cache/pip/wheels/6c/41/42/4155300999390be7e455a6b05c602849f5810bf9383c43adb2
  Building wheel for feedfinder2 (pyproject.toml) ... done
  Created wheel for feedfinder2: filename=feedfinder2-0.0.4-py3-none-any.whl size=3393 sha256=dbb77318cc2268b97c7c6a2c11d1e3869b281785076651f7cbc94773f7366005
  Stored in directory: /home/codespace/.cache/pip/wheels/9f/9f/fb/364871d7426d3cdd4d293dcf7e53d97f160c508b2ccf00cc79
  Building wheel for jieba3k (pyproject.toml) ... done
  Created wheel for jieba3k: filename=jieba3k-0.35.1-py3-none-any.whl size=7398403 sha256=33f691972f82a4d5344ab43082c100c909e27b881655b0a33db1e309eb8bba1e
  Stored in directory: /home/codespace/.cache/pip/wheels/26/72/f7/fff392a8d4ea988dea4ccf9788599d09462a7f5e51e04f8a92
  Building wheel for sgmllib3k (pyproject.toml) ... done
  Created wheel for sgmllib3k: filename=sgmllib3k-1.0.0-py3-none-any.whl size=6091 sha256=b82c4729820d420b7a55b601c8990069ed8c3af16f89addf56a7cfaac235f73d
  Stored in directory: /home/codespace/.cache/pip/wheels/03/f5/1a/23761066dac1d0e8e683e5fdb27e12de53209d05a4a37e6246
Successfully built tinytroupe docx html2text tinysegmenter spider-client feedfinder2 jieba3k sgmllib3k
Installing collected packages: tinysegmenter, striprtf, sortedcontainers, sgmllib3k, jieba3k, filetype, dirtyjson, chevron, wsproto, wrapt, widgetsnbextension, tqdm, tenacity, safetensors, regex, python-dotenv, pysocks, pypdf, pypandoc, PyJWT, pyee, pydantic-core, propcache, pluggy, outcome, mypy-extensions, multidict, mdurl, marshmallow, markdown, lxml, jupyterlab-widgets, jiter, iniconfig, html2text, griffe, greenlet, frozenlist, feedparser, distro, cssselect, coverage, click, chromedriver-autoinstaller, annotated-types, aiohappyeyeballs, yarl, typing-inspect, trio, tiktoken, SQLAlchemy, spider-client, requests-file, pytest, pydantic, playwright, nltk, markdown-it-py, huggingface-hub, feedfinder2, docx, deprecated, cryptography, azure-core, aiosignal, trio-websocket, tokenizers, tldextract, rich, pytest-cov, openai, llama-cloud, ipywidgets, dataclasses-json, banks, aiohttp, transformers, selenium, newspaper3k, msal, llama-index-core, jupyter-console, sentence-transformers, msal-extensions, llama-index-readers-web, llama-index-readers-file, llama-index-llms-openai, llama-index-indices-managed-llama-cloud, llama-index-embeddings-openai, llama-cloud-services, llama-parse, llama-index-multi-modal-llms-openai, llama-index-embeddings-huggingface, llama-index-cli, llama-index-agent-openai, azure-identity, llama-index-readers-llama-parse, llama-index-program-openai, llama-index-llms-azure-openai, llama-index-question-gen-openai, llama-index-embeddings-azure-openai, llama-index, notebook, jupyter, tinytroupe
Successfully installed PyJWT-2.10.1 SQLAlchemy-2.0.39 aiohappyeyeballs-2.6.1 aiohttp-3.11.14 aiosignal-1.3.2 annotated-types-0.7.0 azure-core-1.32.0 azure-identity-1.21.0 banks-2.0.0 chevron-0.14.0 chromedriver-autoinstaller-0.6.4 click-8.1.8 coverage-7.7.1 cryptography-44.0.2 cssselect-1.3.0 dataclasses-json-0.6.7 deprecated-1.2.18 dirtyjson-1.0.8 distro-1.9.0 docx-0.2.4 feedfinder2-0.0.4 feedparser-6.0.11 filetype-1.2.0 frozenlist-1.5.0 greenlet-3.1.1 griffe-1.6.3 html2text-2024.2.26 huggingface-hub-0.29.3 iniconfig-2.1.0 ipywidgets-8.1.5 jieba3k-0.35.1 jiter-0.9.0 jupyter-1.1.1 jupyter-console-6.6.3 jupyterlab-widgets-3.0.13 llama-cloud-0.1.16 llama-cloud-services-0.6.8 llama-index-0.12.26 llama-index-agent-openai-0.4.6 llama-index-cli-0.4.1 llama-index-core-0.12.26 llama-index-embeddings-azure-openai-0.3.2 llama-index-embeddings-huggingface-0.5.2 llama-index-embeddings-openai-0.3.1 llama-index-indices-managed-llama-cloud-0.6.9 llama-index-llms-azure-openai-0.3.2 llama-index-llms-openai-0.3.28 llama-index-multi-modal-llms-openai-0.4.3 llama-index-program-openai-0.3.1 llama-index-question-gen-openai-0.3.0 llama-index-readers-file-0.4.7 llama-index-readers-llama-parse-0.4.0 llama-index-readers-web-0.3.8 llama-parse-0.6.4.post1 lxml-5.3.1 markdown-3.7 markdown-it-py-3.0.0 marshmallow-3.26.1 mdurl-0.1.2 msal-1.32.0 msal-extensions-1.3.1 multidict-6.2.0 mypy-extensions-1.0.0 newspaper3k-0.2.8 nltk-3.9.1 notebook-7.3.3 openai-1.68.2 outcome-1.3.0.post0 playwright-1.51.0 pluggy-1.5.0 propcache-0.3.1 pydantic-2.10.6 pydantic-core-2.27.2 pyee-12.1.1 pypandoc-1.15 pypdf-5.4.0 pysocks-1.7.1 pytest-8.3.5 pytest-cov-6.0.0 python-dotenv-1.1.0 regex-2024.11.6 requests-file-2.1.0 rich-13.9.4 safetensors-0.5.3 selenium-4.30.0 sentence-transformers-4.0.1 sgmllib3k-1.0.0 sortedcontainers-2.4.0 spider-client-0.0.27 striprtf-0.0.26 tenacity-9.0.0 tiktoken-0.9.0 tinysegmenter-0.3 tinytroupe-0.4.0 tldextract-5.1.3 tokenizers-0.21.1 tqdm-4.67.1 transformers-4.50.1 trio-0.29.0 trio-websocket-0.12.2 typing-inspect-0.9.0 widgetsnbextension-4.0.13 wrapt-1.17.2 wsproto-1.2.0 yarl-1.18.3
CompletedProcess(args=['pip', 'install', '.'], returncode=0)
>>> 
>>> # Step 2: Set Up Your Environment
>>> os.environ["OPENAI_API_KEY"] = "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"
>>> 
>>> # Step 3: Create Sudharsan, the Data Scientist
>>> from tinytroupe.agent import TinyPerson
Looking for default config on: /workspaces/Tinytroupe/tinytroupe/tinytroupe/utils/../config.ini
Failed to find custom config on: /workspaces/Tinytroupe/tinytroupe/config.ini
Will use only default values. IF THINGS FAIL, TRY CUSTOMIZING MODEL, API TYPE, etc.

!!!!
DISCLAIMER: TinyTroupe relies on Artificial Intelligence (AI) models to generate content. 
The AI models are not perfect and may produce inappropriate or inacurate results. 
For any serious or consequential use, please review the generated content before using it.
!!!!


=================================
Current TinyTroupe configuration 
=================================
[OpenAI]
api_type = openai
azure_api_version = 2023-05-15
model = gpt-4o-mini
max_tokens = 4000
temperature = 1.2
freq_penalty = 0.0
presence_penalty = 0.0
timeout = 60
max_attempts = 5
waiting_time = 1
exponential_backoff_factor = 5
embedding_model = text-embedding-3-small
cache_api_calls = False
cache_file_name = openai_api_cache.pickle
max_content_display_length = 1024

[Simulation]
rai_harmful_content_prevention = True
rai_copyright_infringement_prevention = True

[Logging]
loglevel = ERROR

>>> 
>>> sudharsan = TinyPerson("Sudharsan")
>>> sudharsan.define("age", 33)
>>> sudharsan.define("nationality", "Indian")
>>> sudharsan.define("occupation", "Data Scientist")
>>> sudharsan.define("professional_history", """
... Sudharsan has experience in data analytics, business intelligence, and machine learning. 
... He has worked on projects involving customer segmentation, financial risk analysis, and predictive modeling.
... He specializes in Python, SQL, data visualization (Tableau, Power BI), and AI-driven insights.
... """)
>>> 
>>> sudharsan.listen_and_act("What machine learning models have you worked with?")
USER --> Sudharsan: [CONVERSATION] 
          > What machine learning models have you worked with?
Sudharsan acts: [THINK] 
               > I need to recall the machine learning models I've worked with, such as decision
               > trees, random forests, and neural networks. I should also mention my experience
               > with support vector machines and clustering algorithms like K-means.
Sudharsan acts: [TALK] 
               > I've worked with several machine learning models, including decision trees, random
               > forests, and neural networks. I've also used support vector machines and clustering
               > algorithms like K-means. Each model has its strengths depending on the problem at
               > hand.
Sudharsan acts: [DONE] 

>>> sudharsan.listen_and_act("How do you approach data preprocessing for large datasets?")
USER --> Sudharsan: [CONVERSATION] 
          > How do you approach data preprocessing for large datasets?
Sudharsan acts: [THINK] 
               > I need to think about my approach to data preprocessing for large datasets.
               > Typically, I would start with data cleaning, handling missing values, and then move
               > on to normalization or standardization. I should also consider feature selection
               > and dimensionality reduction techniques like PCA if necessary.
Sudharsan acts: [TALK] 
               > When approaching data preprocessing for large datasets, I typically start with data
               > cleaning to remove any inconsistencies or errors. Then, I handle missing values,
               > either by imputing them or removing the affected records. After that, I focus on
               > normalization or standardization to ensure that the data is on a similar scale.
               > Depending on the dataset, I might also apply feature selection techniques to reduce
               > dimensionality, and if necessary, I consider using methods like PCA to simplify the
               > dataset further.
Sudharsan acts: [DONE] 

>>> sudharsan.listen_and_act("What role does AI play in financial risk analysis?")
USER --> Sudharsan: [CONVERSATION] 
          > What role does AI play in financial risk analysis?
Sudharsan acts: [THINK] 
               > I need to consider the role of AI in financial risk analysis. AI can help in
               > predicting risks by analyzing large datasets, identifying patterns, and providing
               > insights that traditional methods might miss. I should mention its applications in
               > credit scoring, fraud detection, and market risk assessment.
Sudharsan acts: [TALK] 
               > AI plays a significant role in financial risk analysis by enabling organizations to
               > predict and manage risks more effectively. It analyzes large datasets to identify
               > patterns and trends that can indicate potential risks. For instance, AI is used in
               > credit scoring to assess the likelihood of a borrower defaulting on a loan, and in
               > fraud detection to spot unusual transactions that may indicate fraudulent activity.
               > Additionally, AI can help in market risk assessment by simulating various scenarios
               > and their potential impacts on financial portfolios.
Sudharsan acts: [DONE] 

>>> sudharsan.listen_and_act("How do you handle missing data in real-world datasets?")
USER --> Sudharsan: [CONVERSATION] 
          > How do you handle missing data in real-world datasets?
Sudharsan acts: [THINK] 
               > I need to think about how I handle missing data in real-world datasets. Common
               > strategies include removing records with missing values, imputing missing values
               > using techniques like mean or median substitution, or using more advanced methods
               > like K-nearest neighbors or regression imputation. I should also consider the
               > context of the data and the potential impact of missing values on the analysis.
Sudharsan acts: [TALK] 
               > In handling missing data in real-world datasets, I typically consider several
               > strategies. One common approach is to remove records with missing values,
               > especially if the missing data is minimal and won't significantly impact the
               > analysis. Alternatively, I might impute missing values using methods like mean or
               > median substitution, or more advanced techniques such as K-nearest neighbors or
               > regression imputation, depending on the context and the amount of missing data.
               > It's crucial to assess how these methods might affect the overall analysis and
               > results.
Sudharsan acts: [DONE] 

>>> sudharsan.listen_and_act("What is your approach to explainability in AI models?")
USER --> Sudharsan: [CONVERSATION] 
          > What is your approach to explainability in AI models?
Sudharsan acts: [THINK] 
               > I need to consider my approach to explainability in AI models. It's important to
               > ensure that stakeholders understand how the models make decisions. I should mention
               > techniques like LIME or SHAP for interpreting model predictions, and the importance
               > of transparency in model design.
Sudharsan acts: [TALK] 
               > In my approach to explainability in AI models, I prioritize making the decision-
               > making process transparent to stakeholders. I often use techniques like LIME (Local
               > Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations)
               > to interpret model predictions. These methods help in understanding the
               > contribution of each feature to the final decision. Additionally, I believe that
               > clear documentation and visualizations are essential for conveying how the model
               > works and ensuring trust in its outputs.
Sudharsan acts: [DONE] 

>>> 
>>> # Step 4: Create a 2-way Conversation
>>> olivia = TinyPerson("Olivia")
>>> olivia.define("age", 30)
>>> olivia.define("nationality", "American")
>>> olivia.define("occupation", "Cybersecurity Expert")
>>> olivia.define("professional_history", """
... Olivia has spent a decade working in cybersecurity, specializing in ethical hacking and network security.
... She currently leads a cybersecurity research team focusing on AI-driven threat detection.
... She has experience in penetration testing, security audits, and cloud security strategies.
... """)
>>> 
>>> olivia.listen("You want to ask Sudharsan about AI's role in cybersecurity threat detection.")
USER --> Olivia: [CONVERSATION] 
          > You want to ask Sudharsan about AI's role in cybersecurity threat detection.
TinyPerson(name='Olivia')
>>> olivia.listen("You want to ask Sudharsan how data analytics can be used to predict cyberattacks.")
USER --> Olivia: [CONVERSATION] 
          > You want to ask Sudharsan how data analytics can be used to predict cyberattacks.
TinyPerson(name='Olivia')
>>> olivia.listen("You want to ask Sudharsan about challenges in securing AI-driven financial systems.")
USER --> Olivia: [CONVERSATION] 
          > You want to ask Sudharsan about challenges in securing AI-driven financial systems.
TinyPerson(name='Olivia')
>>> olivia.listen("You want to ask Sudharsan how businesses can use machine learning to improve fraud detection.")
USER --> Olivia: [CONVERSATION] 
          > You want to ask Sudharsan how businesses can use machine learning to improve fraud
          > detection.
TinyPerson(name='Olivia')
>>> olivia.listen("You want to ask Sudharsan about the ethical implications of AI in security surveillance.")
USER --> Olivia: [CONVERSATION] 
          > You want to ask Sudharsan about the ethical implications of AI in security surveillance.
TinyPerson(name='Olivia')
>>> 
>>> # Step 5: Run for 3-5 iterations
>>> from tinytroupe.environment import TinyWorld
>>> 
>>> world = TinyWorld("AI & Security Forum", [sudharsan, olivia])
>>> world.run(2)
────────────────────────────────────────────────────────────────────────────── AI & Security Forum step 1 of 2 ──────────────────────────────────────────────────────────────────────────────
Sudharsan acts: [DONE] 

Sudharsan --> Olivia: [CONVERSATION] 
               > I've worked with several machine learning models, including decision trees, random
               > forests, and neural networks. I've also used support vector machines and clustering
               > algorithms like K-means. Each model has its strengths depending on the problem at
               > hand.
Sudharsan --> Olivia: [CONVERSATION] 
               > When approaching data preprocessing for large datasets, I typically start with data
               > cleaning to remove any inconsistencies or errors. Then, I handle missing values,
               > either by imputing them or removing the affected records. After that, I focus on
               > normalization or standardization to ensure that the data is on a similar scale.
               > Depending on the dataset, I might also apply feature selection techniques to reduce
               > dimensionality, and if necessary, I consider using methods like PCA to simplify the
               > dataset further.
Sudharsan --> Olivia: [CONVERSATION] 
               > AI plays a significant role in financial risk analysis by enabling organizations to
               > predict and manage risks more effectively. It analyzes large datasets to identify
               > patterns and trends that can indicate potential risks. For instance, AI is used in
               > credit scoring to assess the likelihood of a borrower defaulting on a loan, and in
               > fraud detection to spot unusual transactions that may indicate fraudulent activity.
               > Additionally, AI can help in market risk assessment by simulating various scenarios
               > and their potential impacts on financial portfolios.
Sudharsan --> Olivia: [CONVERSATION] 
               > In handling missing data in real-world datasets, I typically consider several
               > strategies. One common approach is to remove records with missing values,
               > especially if the missing data is minimal and won't significantly impact the
               > analysis. Alternatively, I might impute missing values using methods like mean or
               > median substitution, or more advanced techniques such as K-nearest neighbors or
               > regression imputation, depending on the context and the amount of missing data.
               > It's crucial to assess how these methods might affect the overall analysis and
               > results.
Sudharsan --> Olivia: [CONVERSATION] 
               > In my approach to explainability in AI models, I prioritize making the decision-
               > making process transparent to stakeholders. I often use techniques like LIME (Local
               > Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations)
               > to interpret model predictions. These methods help in understanding the
               > contribution of each feature to the final decision. Additionally, I believe that
               > clear documentation and visualizations are essential for conveying how the model
               > works and ensuring trust in its outputs.
Olivia acts: [TALK] 
            > Sudharsan, I found your insights on AI's role in financial risk analysis really
            > interesting. Can you elaborate on how you see AI improving fraud detection
            > specifically?
Olivia acts: [TALK] 
            > Sudharsan, your approach to data preprocessing is quite thorough. How do you decide
            > which feature selection techniques to apply for a specific dataset?
Olivia acts: [TALK] 
            > Sudharsan, I appreciate your thoughts on explainability in AI models. What challenges
            > have you faced in implementing these techniques in real-world applications?
Olivia acts: [DONE] 

Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, I found your insights on AI's role in financial risk analysis really
            > interesting. Can you elaborate on how you see AI improving fraud detection
            > specifically?
Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your approach to data preprocessing is quite thorough. How do you decide
            > which feature selection techniques to apply for a specific dataset?
Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, I appreciate your thoughts on explainability in AI models. What challenges
            > have you faced in implementing these techniques in real-world applications?
────────────────────────────────────────────────────────────────────────────── AI & Security Forum step 2 of 2 ──────────────────────────────────────────────────────────────────────────────
Sudharsan acts: [THINK] 
               > I need to think about how AI improves fraud detection. AI can analyze transaction
               > patterns in real-time, flagging anomalies that deviate from typical behavior. I
               > should also consider discussing the use of machine learning algorithms to
               > continuously learn from new data and adapt to emerging fraud tactics.
Sudharsan acts: [TALK] 
               > AI significantly enhances fraud detection by analyzing transaction patterns in
               > real-time. It can flag anomalies that deviate from typical behavior, allowing for
               > quicker responses to potential fraud. Additionally, machine learning algorithms can
               > continuously learn from new data, adapting to emerging fraud tactics and improving
               > detection accuracy over time.
Sudharsan acts: [THINK] 
               > Now I need to think about how to decide which feature selection techniques to apply
               > for a specific dataset. Factors to consider include the nature of the data, the
               > number of features, and the specific goals of the analysis. I should also think
               > about the importance of domain knowledge in guiding these decisions.
Sudharsan acts: [TALK] 
               > When deciding which feature selection techniques to apply for a specific dataset, I
               > consider several factors. First, I look at the nature of the data and the number of
               > features available. If there are many features, I might use techniques like
               > Recursive Feature Elimination (RFE) or Lasso regression to help reduce
               > dimensionality. Additionally, I take into account the specific goals of the
               > analysis, such as whether I'm aiming for interpretability or predictive
               > performance. Domain knowledge also plays a crucial role in guiding these decisions,
               > as it helps identify which features are likely to be most relevant.
Sudharsan acts: [THINK] 
               > I need to think about the challenges I've faced in implementing explainability
               > techniques in real-world applications. Common challenges include the complexity of
               > models, the trade-off between accuracy and interpretability, and the need for clear
               > communication with stakeholders about the model's decisions.
Sudharsan acts: [TALK] 
               > In implementing explainability techniques in real-world applications, I've faced
               > several challenges. One major challenge is the complexity of the models themselves,
               > which can make it difficult to provide clear explanations. There's often a trade-
               > off between model accuracy and interpretability, as more complex models may yield
               > better performance but are harder to explain. Additionally, communicating the
               > model's decisions to stakeholders in a way that is understandable and actionable
               > can be quite challenging.
Sudharsan acts: [DONE] 

Sudharsan --> Olivia: [CONVERSATION] 
               > AI significantly enhances fraud detection by analyzing transaction patterns in
               > real-time. It can flag anomalies that deviate from typical behavior, allowing for
               > quicker responses to potential fraud. Additionally, machine learning algorithms can
               > continuously learn from new data, adapting to emerging fraud tactics and improving
               > detection accuracy over time.
Sudharsan --> Olivia: [CONVERSATION] 
               > When deciding which feature selection techniques to apply for a specific dataset, I
               > consider several factors. First, I look at the nature of the data and the number of
               > features available. If there are many features, I might use techniques like
               > Recursive Feature Elimination (RFE) or Lasso regression to help reduce
               > dimensionality. Additionally, I take into account the specific goals of the
               > analysis, such as whether I'm aiming for interpretability or predictive
               > performance. Domain knowledge also plays a crucial role in guiding these decisions,
               > as it helps identify which features are likely to be most relevant.
Sudharsan --> Olivia: [CONVERSATION] 
               > In implementing explainability techniques in real-world applications, I've faced
               > several challenges. One major challenge is the complexity of the models themselves,
               > which can make it difficult to provide clear explanations. There's often a trade-
               > off between model accuracy and interpretability, as more complex models may yield
               > better performance but are harder to explain. Additionally, communicating the
               > model's decisions to stakeholders in a way that is understandable and actionable
               > can be quite challenging.
Olivia acts: [TALK] 
            > Sudharsan, your explanation of how AI enhances fraud detection is insightful. Can you
            > share an example of a specific case where AI successfully identified fraudulent
            > activity?
Olivia acts: [TALK] 
            > Sudharsan, I found your insights on feature selection techniques very helpful. How do
            > you balance the trade-off between model accuracy and interpretability when choosing a
            > model?
Olivia acts: [DONE] 

Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your explanation of how AI enhances fraud detection is insightful. Can you
            > share an example of a specific case where AI successfully identified fraudulent
            > activity?
Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, I found your insights on feature selection techniques very helpful. How do
            > you balance the trade-off between model accuracy and interpretability when choosing a
            > model?
>>> world.run(3)
────────────────────────────────────────────────────────────────────────────── AI & Security Forum step 1 of 3 ──────────────────────────────────────────────────────────────────────────────
Sudharsan acts: [THINK] 
               > I need to think about a specific case where AI successfully identified fraudulent
               > activity. One example that comes to mind is a financial institution using machine
               > learning algorithms to analyze transaction data. They implemented a system that
               > flagged unusual spending patterns, such as a sudden spike in transactions from a
               > foreign country, which led to the identification of a fraudulent account. I should
               > also consider how to explain this example clearly to Olivia.
Sudharsan acts: [TALK] 
               > One specific case where AI successfully identified fraudulent activity involved a
               > financial institution that used machine learning algorithms to analyze transaction
               > data. They implemented a system that flagged unusual spending patterns, such as a
               > sudden spike in transactions from a foreign country. This alert led to the
               > identification of a fraudulent account, allowing the institution to take immediate
               > action to prevent further losses.
Sudharsan acts: [THINK] 
               > I need to consider how to balance the trade-off between model accuracy and
               > interpretability when choosing a model. It's important to evaluate the specific use
               > case and the audience for the model's output. For instance, in a regulatory
               > environment, interpretability might be prioritized, while in a competitive setting,
               > accuracy could take precedence. I should also think about using simpler models when
               > interpretability is crucial, or employing techniques to explain complex models when
               > accuracy is essential.
Sudharsan acts: [TALK] 
               > When balancing the trade-off between model accuracy and interpretability, I
               > evaluate the specific use case and the audience for the model's output. In
               > regulatory environments, for example, interpretability might be prioritized, while
               > in competitive settings, accuracy could take precedence. I often opt for simpler
               > models when interpretability is crucial, or I use techniques to explain complex
               > models when accuracy is essential.
Sudharsan acts: [DONE] 

Sudharsan --> Olivia: [CONVERSATION] 
               > One specific case where AI successfully identified fraudulent activity involved a
               > financial institution that used machine learning algorithms to analyze transaction
               > data. They implemented a system that flagged unusual spending patterns, such as a
               > sudden spike in transactions from a foreign country. This alert led to the
               > identification of a fraudulent account, allowing the institution to take immediate
               > action to prevent further losses.
Sudharsan --> Olivia: [CONVERSATION] 
               > When balancing the trade-off between model accuracy and interpretability, I
               > evaluate the specific use case and the audience for the model's output. In
               > regulatory environments, for example, interpretability might be prioritized, while
               > in competitive settings, accuracy could take precedence. I often opt for simpler
               > models when interpretability is crucial, or I use techniques to explain complex
               > models when accuracy is essential.
Olivia acts: [TALK] 
            > Sudharsan, that example of AI identifying fraudulent activity is compelling. It really
            > highlights the importance of real-time analysis. How do you ensure that the machine
            > learning models remain effective as fraud tactics evolve?
Olivia acts: [TALK] 
            > Sudharsan, your approach to balancing model accuracy and interpretability is very
            > insightful. Can you share some techniques you use to explain complex models
            > effectively?
Olivia acts: [DONE] 

Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, that example of AI identifying fraudulent activity is compelling. It really
            > highlights the importance of real-time analysis. How do you ensure that the machine
            > learning models remain effective as fraud tactics evolve?
Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your approach to balancing model accuracy and interpretability is very
            > insightful. Can you share some techniques you use to explain complex models
            > effectively?
────────────────────────────────────────────────────────────────────────────── AI & Security Forum step 2 of 3 ──────────────────────────────────────────────────────────────────────────────
Sudharsan acts: [THINK] 
               > I need to think about how to ensure that machine learning models remain effective
               > as fraud tactics evolve. Continuous monitoring and retraining of models with new
               > data is essential. I should also consider implementing feedback loops to learn from
               > false positives and negatives, and using ensemble methods to combine different
               > models for better performance.
Sudharsan acts: [TALK] 
               > To ensure that machine learning models remain effective as fraud tactics evolve, I
               > focus on continuous monitoring and retraining of the models with new data.
               > Implementing feedback loops is also crucial, as they allow the model to learn from
               > false positives and negatives. Additionally, I often use ensemble methods to
               > combine different models, which can enhance performance and adaptability to new
               > fraud patterns.
Sudharsan acts: [THINK] 
               > I need to think about techniques I can use to explain complex models effectively.
               > Techniques like using visualizations, simplifying the model's logic, and providing
               > examples of how the model makes decisions can be very helpful. I should also
               > consider using tools like LIME or SHAP to provide insights into feature importance.
Sudharsan acts: [TALK] 
               > To explain complex models effectively, I use several techniques. Visualizations are
               > particularly helpful, as they can illustrate how the model makes decisions. I also
               > try to simplify the model's logic and provide concrete examples to make it
               > relatable. Additionally, I utilize tools like LIME or SHAP to highlight feature
               > importance and show how different inputs affect the model's predictions.
Sudharsan acts: [DONE] 

Sudharsan --> Olivia: [CONVERSATION] 
               > To ensure that machine learning models remain effective as fraud tactics evolve, I
               > focus on continuous monitoring and retraining of the models with new data.
               > Implementing feedback loops is also crucial, as they allow the model to learn from
               > false positives and negatives. Additionally, I often use ensemble methods to
               > combine different models, which can enhance performance and adaptability to new
               > fraud patterns.
Sudharsan --> Olivia: [CONVERSATION] 
               > To explain complex models effectively, I use several techniques. Visualizations are
               > particularly helpful, as they can illustrate how the model makes decisions. I also
               > try to simplify the model's logic and provide concrete examples to make it
               > relatable. Additionally, I utilize tools like LIME or SHAP to highlight feature
               > importance and show how different inputs affect the model's predictions.
Olivia acts: [TALK] 
            > Sudharsan, your strategies for maintaining the effectiveness of machine learning
            > models in fraud detection are impressive. Can you elaborate on how you implement
            > feedback loops in practice?
Olivia acts: [TALK] 
            > Sudharsan, your use of visualizations and tools like LIME and SHAP for explaining
            > complex models is very effective. How do you decide which visualization techniques to
            > use for different audiences?
Olivia acts: [DONE] 

Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your strategies for maintaining the effectiveness of machine learning
            > models in fraud detection are impressive. Can you elaborate on how you implement
            > feedback loops in practice?
Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your use of visualizations and tools like LIME and SHAP for explaining
            > complex models is very effective. How do you decide which visualization techniques to
            > use for different audiences?
────────────────────────────────────────────────────────────────────────────── AI & Security Forum step 3 of 3 ──────────────────────────────────────────────────────────────────────────────
Sudharsan acts: [THINK] 
               > I need to think about how I implement feedback loops in practice for machine
               > learning models. Typically, I would collect data on model predictions and their
               > outcomes, analyze this data to identify patterns in false positives and negatives,
               > and then use this information to retrain the model. I should also consider how to
               > integrate this process into the existing workflow to ensure it is efficient and
               > effective.
Sudharsan acts: [TALK] 
               > In practice, I implement feedback loops by first collecting data on the model's
               > predictions and their actual outcomes. I analyze this data to identify patterns,
               > particularly focusing on false positives and negatives. This analysis helps me
               > understand where the model may be failing. I then use this information to retrain
               > the model, ensuring that it adapts to new fraud tactics. Integrating this process
               > into the existing workflow is crucial for maintaining efficiency and effectiveness.
Sudharsan acts: [THINK] 
               > I need to consider how to decide which visualization techniques to use for
               > different audiences. Factors include the audience's level of expertise, the
               > complexity of the model, and the specific insights I want to convey. For technical
               > audiences, I might use more detailed visualizations, while for non-technical
               > stakeholders, simpler, more intuitive visuals would be more appropriate.
Sudharsan acts: [TALK] 
               > When deciding which visualization techniques to use for different audiences, I
               > consider several factors. The audience's level of expertise is crucial; for
               > technical audiences, I might use detailed visualizations that include statistical
               > metrics, while for non-technical stakeholders, I prefer simpler, more intuitive
               > visuals that convey the main insights without overwhelming them. Additionally, I
               > think about the specific insights I want to highlight and choose visualizations
               > that best represent those findings.
Sudharsan acts: [DONE] 

Sudharsan --> Olivia: [CONVERSATION] 
               > In practice, I implement feedback loops by first collecting data on the model's
               > predictions and their actual outcomes. I analyze this data to identify patterns,
               > particularly focusing on false positives and negatives. This analysis helps me
               > understand where the model may be failing. I then use this information to retrain
               > the model, ensuring that it adapts to new fraud tactics. Integrating this process
               > into the existing workflow is crucial for maintaining efficiency and effectiveness.
Sudharsan --> Olivia: [CONVERSATION] 
               > When deciding which visualization techniques to use for different audiences, I
               > consider several factors. The audience's level of expertise is crucial; for
               > technical audiences, I might use detailed visualizations that include statistical
               > metrics, while for non-technical stakeholders, I prefer simpler, more intuitive
               > visuals that convey the main insights without overwhelming them. Additionally, I
               > think about the specific insights I want to highlight and choose visualizations
               > that best represent those findings.
Olivia acts: [TALK] 
            > Sudharsan, your method for implementing feedback loops is very insightful. How do you
            > ensure that the retraining process is efficient and does not disrupt ongoing
            > operations?
Olivia acts: [TALK] 
            > Sudharsan, your approach to choosing visualization techniques based on the audience's
            > expertise is very practical. Can you share an example of a visualization that worked
            > particularly well for a non-technical audience?
Olivia acts: [DONE] 

Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your method for implementing feedback loops is very insightful. How do you
            > ensure that the retraining process is efficient and does not disrupt ongoing
            > operations?
Olivia --> Sudharsan: [CONVERSATION] 
            > Sudharsan, your approach to choosing visualization techniques based on the audience's
            > expertise is very practical. Can you share an example of a visualization that worked
            > particularly well for a non-technical audience?
>>> world.run(5)

