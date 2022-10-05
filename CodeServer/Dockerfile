FROM codercom/code-server:latest

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension scala-lang.scala
RUN code-server --install-extension scalameta.metals
RUN code-server --install-extension hookyqr.beautify
RUN code-server --install-extension mgmcdermott.vscode-language-babel

RUN sudo apt-get update
RUN sudo apt-get install default-jdk -y
RUN sudo apt-get install gnupg -y

RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
RUN echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
RUN curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
RUN sudo apt-get update
RUN sudo apt-get install sbt
RUN sbt sbtVersion

RUN sudo apt-get install nodejs -y
RUN sudo apt-get install npm -y
RUN sudo apt-get install python3-pip -y

# Set locales
RUN sudo sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

RUN type -p curl >/dev/null || sudo apt install curl -y
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y