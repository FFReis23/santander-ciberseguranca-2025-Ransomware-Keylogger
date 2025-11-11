Projeto: Ambiente Seguro de Estudos sobre Ransomware e Keylogger

Bootcamp - Santander - Cibersegurança 2025

Autor: Fabio Ferreira Reis

Data: 2025-11-11

Escopo

Implementar e/ou documentar duas simulações educativas em Python (em ambiente isolado), demonstrando comportamentos típicos de ransomware e keylogger de 
forma segura e reversível, e produzir um relatório com reflexões sobre defesa e mitigação.

Ransomware Revealed: A Beginner’s Guide to Protecting and Recovering from Ransomware Attacks (Hassan, 2019) define o ransomware assim:
Ransomware é uma categoria de malware que pode criptografar os arquivos do computador e de dispositivos móveis até que um resgate seja pago para desbloqueá‑los.

Keylogger (tanto de hardware quanto de software): é usado para registrar as atividades da vítima no computador — por meio de gravações de voz, capturas de tela, 
microfones e câmeras — visando monitoramento contínuo e recolha de dados sensíveis.

Aviso Ético e Legal

Este projeto deve ser executado apenas em ambiente isolado e controlado (laboratório) com máquinas que você possui ou tem autorização explícita para testar. 
Qualquer tentativa de ataque contra sistemas sem autorização é ilegal. Use este material apenas para fins educativos e de teste em ambientes de laboratório.

Tecnologias e Ferramentas Utilizadas :

- IDE: PyCharm Community Edition — ambiente usado para desenvolver, depurar e organizar os scripts Python.
- Linguagem: Python 3.10.12 — implementação das simulações e scripts utilitários.
- Sistema operacional: Ubuntu (Linux) — máquina de desenvolvimento e execução em ambiente isolado.
- Bibliotecas/Módulos Python: cryptography, os, time, pynput, smtplib, email.mime.text, threading
- Conta de e‑mail para envio de testes: conta Gmail criada exclusivamente para laboratório e configurada com Senha de App (App Password) para automação de envio.  


Mitigações e contramedidas :

- Antivírus e Antimalware Atualizados: detectam comportamentos suspeitos, como criptografia em massa ou captura de teclas.
- Firewall e Controle de Rede: bloqueiam conexões de saída não autorizadas, evitando exfiltração de dados.
- Princípio do Menor Privilégio: limitar permissões de usuário impede que scripts maliciosos causem danos críticos.
- Backup Frequente e Isolado: garante a recuperação de arquivos caso ocorra criptografia indevida.
- Sandboxing e Máquinas Virtuais: testam códigos suspeitos em ambientes isolados, protegendo sistemas reais.
- Monitoramento e Logs: ajudam a identificar comportamentos anormais, como modificação de arquivos ou gravação de teclas.
- Conscientização do Usuário: treinar usuários para evitar práticas inseguras, como clicar em anexos ou links desconhecidos.
- Atualizações e Patches: manter sistemas e softwares atualizados fecha vulnerabilidades exploráveis.

Arquivos que serão incluídos neste repositório:

- screenshots/ — prints dos resultados dos testes das simulações em Python, mostrando logs, ransom notes, arquivos modificados e execução dos scripts no PyCharm ou terminal do Ubuntu.
- wordlists/ — exemplos de listas utilizadas nos testes educativos; contêm somente arquivos de teste, sem dados reais ou sensíveis.
- reports/ — saídas geradas pelos scripts de simulação e logs relevantes, como registros de operações do ransomware e keylogger reversível, demonstrando o comportamento controlado dos
experimentos.

Conclusão 

Este projeto demonstrou, em ambiente controlado, como funcionam as ameaças de ransomware e keylogger e como podemos aplicar defesas práticas. Ao experimentar com scripts em Python, ficou 
claro que a combinação entre boas práticas técnicas, monitoramento ativo e educação de usuários é essencial para mitigar riscos digitais.

















Conclusão

