Projeto: Ambiente Seguro de Estudos sobre Ransomware e Keylogger

Bootcamp - Santander - Cibersegurança 2025

Autor: Fabio Ferreira Reis

Data: 2025-11-11

Escopo

Implementar e/ou documentar duas simulações educativas em Python (em ambiente isolado), demonstrando comportamentos típicos de ransomware e keylogger de 
forma segura e reversível, e produzir um relatório com reflexões sobre defesa e mitigação.

Segundo Preston e Saylor (2026),o ransomware tornou-se um dos mais significativos do mundo ameaças à segurança cibernética, mantendo indivíduos, empresas e 
até mesmo governos reféns criptografando dados e sistemas críticos, exigindo pagamento por chaves de descriptografia e extorsão adicional de suas vítimas 
divulgando publicamente seus dados. Imagine acordar e encontrar todos os seus arquivos trancado e um relógio em contagem regressiva até você pagar ou perder 
tudo.
Ransomware é um software malicioso (malware) projetado para bloquear o acesso para um sistema de computador ou criptografar seus dados até que um resgate 
seja pago. No seu núcleo, o ransomware se infiltra em um sistema de computador geralmente por meio de meios enganosos, como e-mails de phishing ou downloads
maliciosos e então criptografa os arquivos da vítima, tornando-os inacessíveis.

Segundo Singh et al. (2021),Keylogger é basicamente um tipo particular de spyware que pode gravar tudo o que você digita em seu teclado. Embora seja uma 
ferramenta comum para as empresas, o departamento de tecnologia da informação do a corporação usa o software de registro de chaves para fins de solução de 
problemas ou também é usado para ficar de olho sobre atividades suspeitas do funcionário

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

- screenshots/ — prints dos resultados dos testes das simulações em Python, mostrando logs, ransom notes, arquivos modificados e execução dos scripts no PyCharm ou
terminal do Ubuntu.
- wordlists/ — exemplos de listas utilizadas nos testes educativos; contêm somente arquivos de teste, sem dados reais ou sensíveis.
- reports/ — saídas geradas pelos scripts de simulação e logs relevantes, como registros de operações do ransomware e keylogger reversível, demonstrando o comportamento
controlado dos experimentos.

Conclusão 

O projeto proporcionou uma compreensão prática e segura sobre o funcionamento de ransomware e keyloggers, destacando a importância de ambientes controlados para fins educativos.
As simulações em Python mostraram como ataques simples podem comprometer sistemas desprotegidos e reforçaram o valor de estratégias preventivas, como backups, monitoramento constante 
e educação em segurança cibernética.

Referências bibliográficas 

PRESTON, W. Curtis; SAYLOR, Michael. Learning Ransomware Response & Recovery. Sebastopol: O’Reilly Media, 2026.

SINGH, Arjun; CHOUDHARY, Pushpa; SINGH, Akhilesh Kumar; TYAGI, Dheerendra Kumar. Keylogger Detection and Prevention. In: 3rd International Conference on Computational & Experimental Methods 
in Mechanical Engineering (ICCEMME), 11–13 fev. 2021, Uttar Pradesh, India. Journal of Physics: Conference Series, v. 2007, p. 012005, 2021. DOI: 10.1088/1742-6596/2007/1/012005.


