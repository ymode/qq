# qq
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ymode/qq/pylint.yml)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ymode/qq) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/ymode/qq) ![GitHub watchers](https://img.shields.io/github/watchers/ymode/qq)



```qq``` Quick Question - LLM in the terminal.

<img src="https://github.com/user-attachments/assets/60dce499-561a-4ad0-b98a-67adaaf48e3a" width="150"/>

# About

<div align="center">
  

qq is a markdown rich terminal based LLM interface - so you never have to leave the terminal! qq supports [gpt-4o-mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) and [llama-3.1-8b](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct?text=can+llama+accept+openai+api+syntax)

<br>

  
<img width="700" alt="image" src="https://github.com/user-attachments/assets/1d6b7cd4-f927-4240-8a23-54725989a6d7">
 
   
   _looks and works great in [warp](https://www.warp.dev)_
   
 </div>


# Features

🎨 Markdown support in your terminal

🧠 gpt-4o-mini (default LLM)

🦙 Now with llama-3 support! (optional)

⌨️ Prompt engineering layer to ensure terminal/linux based responses

💻 Stay in terminal

# Use
```bash
qq how do I list files in terminal by size?
# or with llama
qq --model llama how do I exit vim?
# disable spinner (good for scripts)
qq --no-spinner whoami
```




# Setup

⏳ Coming Soon - 🐳 A Docker Version! 

🔑 Ensure your [OpenAI](https://openai.com/api/) API Key is exported in the following format: ```export OPENAI_API_KEY=your openai key```

💻 Automatic Setup: In your Term, paste the following (target qql.py instead of qq.py if you want to use llama-3 instead of gpt-4o-mini)

```export OPENAI_API_KEY=your OpenAI API key
git clone https://github.com/ymode/qq.git
cd qq
pip install -r requirements.txt
chmod +x qq
sudo mv qq /usr/local/bin/
```


# Support
The best way to support this project is to contribute! But if you would like to buy me a coffee, there is a link below.

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ymode)

# Credits

[OpenAI gpt-4o-mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/)

[dotenv](https://github.com/motdotla/dotenv)

[rich terminal markdown](https://github.com/Textualize/rich)

[halo - beautiful spinners](https://github.com/manrajgrover/halo)
