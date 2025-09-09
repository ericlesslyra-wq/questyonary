from flask import Flask, render_template, request

app = Flask(__name__)

# Gabarito
questions = [
    {
        "text": "Qual é a principal ferramenta usada pelo NOC da Lyra para monitoramento?",
        "options": ["Grafana", "Zabbix", "Kibana", "Prometheus"],
        "answer": "Zabbix"
    },
    {
        "text": "Qual é a principal função do NOC na Lyra Network?",
        "options": ["Desenvolver sistemas", "Vender equipamentos", "Monitorar os serviços em tempo real", "Atender clientes"],
        "answer": "Monitorar os serviços em tempo real"
    },
    {
        "text": "Qual o número de telefone fixo para contato com o NOC da Lyra?",
        "options": ["(11) 9999-9999", "(11) 3336-9201", "0800 888 5972", "(11) 98447-2274"],
        "answer": "(11) 3336-9201"
    },
    {
        "text": "O que deve ser feito quando um alarme com severidade \"Alta\" é gerado?",
        "options": ["Ignorar", "Enviar por e-mail apenas", "Acionar o sobreaviso", "Reiniciar o servidor"],
        "answer": "Acionar o sobreaviso"
    },
    {
        "text": "Quais áreas fazem parte do departamento de TI da Lyra?",
        "options": ["RH, Financeiro, Comercial", "NOC, Produção, Suporte, Desenvolvimento", "Jurídico, Logística, Marketing", "Infraestrutura, Manutenção, Contábil"],
        "answer": "NOC, Produção, Suporte, Desenvolvimento"
    },
    {
        "text": "O que é o LSS (Lyra Secure Switch)?",
        "options": ["Um antivírus corporativo", "Um sistema de backup automatizado", "Um serviço que usa comunicação IP com autenticação SSL", "Um modelo de POS físico"],
        "answer": "Um serviço que usa comunicação IP com autenticação SSL"
    },
    {
        "text": "Qual informação não está disponível nas telas de monitoramento DIAL?",
        "options": ["Volume de transações", "Nome da operadora", "Alertas em tempo real", "Data center de origem"],
        "answer": "Data center de origem"
    },
    {
        "text": "Qual dos itens abaixo não é um alerta crítico citado no material?",
        "options": ["Link Down", "Restart de servidores", "Atualização de senha", "Nenhuma conexão X.25"],
        "answer": "Atualização de senha"
    },
    {
        "text": "O reconhecimento de um incidente no Zabbix serve para:",
        "options": ["Reiniciar o sistema", "Esconder o alarme", "Informar que alguém está tratando do evento", "Deletar o histórico"],
        "answer": "Informar que alguém está tratando do evento"
    },
    {
        "text": "O acesso ao Zabbix pode ser feito por qual URL?",
        "options": ["https://zabbix.lyra.com.br", "https://monitoramento.lyra-network.com.br/index.php", "https://lyra.zabbix.com", "https://status.lyra.com"],
        "answer": "https://monitoramento.lyra-network.com.br/index.php"
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_answers = request.form
        result = []
        for i, q in enumerate(questions):
            selected = user_answers.get(f'q{i}')
            correct = q['answer']
            result.append({
                'question': q['text'],
                'selected': selected,
                'correct': correct,
                'is_correct': selected == correct
            })
    return render_template('index.html', questions=questions, result=result)

if __name__ == '__main__':
    app.run(debug=True)
