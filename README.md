
# Banking System in Python

This project implements a basic banking system in Python, allowing a user to perform the following operations:
- **Deposit**: Allows the user to deposit a positive amount of money into their account.
- **Withdrawal**: Limits the user to 3 daily withdrawals, with a maximum amount of R$500 per transaction. If the user has insufficient funds, the withdrawal will not be allowed.
- **Statement**: Displays the user’s transaction history (deposits and withdrawals) along with the current balance.

## Project Details
- This is the first version of the banking system, and it works with only one user.
- No identification (like agency or account number) is required, as all transactions are associated with the single user.
- Deposits and withdrawals are stored and displayed when the user requests a statement.

## System Operations
1. **Depositing**: Enter the amount to be deposited. The amount must be greater than 0.
2. **Withdrawing**: Enter the amount to withdraw. The system will check if the user has enough balance and if the amount is within the daily limit.
3. **Statement**: View the list of transactions and the current balance.

## Running the Project
To run the system, you need to have Python installed on your machine. Clone this repository, navigate to the project directory, and run the script:

```bash
python Challenge-DIO-01-Bank-System-in-Python.py
```

## Technologies Used
- **Python**: The system was built using basic Python programming, focusing on flow control, user input, and variable manipulation.

## Future Enhancements
- Implementing multiple users with unique accounts.
- Adding authentication (PIN or password).
- Including interest calculation for savings accounts.
- Allowing transfers between accounts.

---

This project is designed to practice basic Python concepts and simulate a simple banking system. Future versions will add more complexity and functionality.

###############

# Sistema Bancário em Python

Este projeto implementa um sistema bancário básico em Python, permitindo que um usuário realize as seguintes operações:
- **Depósito**: Permite que o usuário deposite um valor positivo em sua conta.
- **Saque**: Limita o usuário a 3 saques diários, com um valor máximo de R$500 por transação. Se o usuário não tiver saldo suficiente, o saque não será permitido.
- **Extrato**: Exibe o histórico de transações do usuário (depósitos e saques) junto com o saldo atual.

## Detalhes do Projeto
- Esta é a primeira versão do sistema bancário, e ele funciona com apenas um usuário.
- Não é necessária nenhuma identificação (como agência ou número de conta), já que todas as transações estão associadas a um único usuário.
- Depósitos e saques são armazenados e exibidos quando o usuário solicita o extrato.

## Operações do Sistema
1. **Depósito**: Insira o valor a ser depositado. O valor deve ser maior que 0.
2. **Saque**: Insira o valor a ser sacado. O sistema verificará se o usuário tem saldo suficiente e se o valor está dentro do limite diário.
3. **Extrato**: Visualize a lista de transações e o saldo atual.

## Executando o Projeto
Para executar o sistema, você precisa ter o Python instalado em sua máquina. Clone este repositório, navegue até o diretório do projeto e execute o script:

```bash
python Challenge-DIO-01-Bank-System-in-Python.py
```

## Tecnologias Utilizadas
- **Python**: O sistema foi construído utilizando programação básica em Python, com foco no controle de fluxo, entrada de dados do usuário e manipulação de variáveis.

## Melhorias Futuras
- Implementar múltiplos usuários com contas exclusivas.
- Adicionar autenticação (PIN ou senha).
- Incluir cálculo de juros para contas poupança.
- Permitir transferências entre contas.
---

Este projeto foi desenvolvido para praticar conceitos básicos de Python e simular um sistema bancário simples. Versões futuras adicionarão mais complexidade e funcionalidades.
