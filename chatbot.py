from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer




chatbotfatecano = ChatBot(
    'botfatecano',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.MathematicaEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe, mas não entendi. Estou aprendendo.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri = 'sqlite:///database.sqlite3'
)


treinando_dados_perguntas_e_respostas = open('treinamento/perguntaserespostas.txt').read().splitlines()
treinando_dados_pessoal   = open('treinamento/pessoal.txt').read().splitlines()

treino_dados = treinando_dados_perguntas_e_respostas + treinando_dados_pessoal 


treino = ListTrainer(chatbotfatecano)
treino.train(treino_dados)


#Treinando com dados em portugues
treino_corpus = ChatterBotCorpusTrainer
treino_corpus.train(
    'chatterbot.corpus.portugues'
)