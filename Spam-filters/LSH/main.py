import string
import email
import nltk

nltk.download('stopwords')
punctuations = list(string.punctuation)
stopwords = set(nltk.corpus.stopwords.words('english'))
stemmer = nltk.PorterStemmer()

# Объединение частей письма в список строк
def flatten_to_string(parts):
    ret = []
    if type(parts) == str:
        ret.append(parts)
    elif type(parts) == list:
        for part in parts:
            ret += flatten_to_string(part)
    elif parts.get_content_type == 'text/plain':
        ret += parts.get_payload()
    return ret

# Извлечение темы и содержания письма из 1 письма
def extract_email_text(path):
    # Загрузка одного письма из входного файла
    with open(path, errors='ignore') as f:
        msg = email.message_from_file(f)
    if not msg:
        return ""

    # чтение темы сообщения
    subject = msg['Subject']
    if not subject:
        subject = ""

    # чтение самого сообщения
    body = ' '.join(m for m in flatten_to_string(msg.get_payload()) if type(m) == str)
    if not body:
        body = ""

    return subject + ' ' + body

# обработка одного письма для прелбразования слов в слова-токены
def load(path):
    email_text = extract_email_text(path)
    if not email_text:
        return []

    # разбивка сообщения на токены
    tokens = nltk.word_tokenize(email_text)

    # удаление знаков препинания из токенов
    tokens = [i.strip("".join(punctuations)) for i in tokens if i not in punctuations]

    # удаление стопслов и выделение основ токенов
    if len(tokens) > 2:
        return [stemmer.stem(w) for w in tokens if w not in stopwords]
    return []

