from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {
            'id' : 1,
            'nome' : 'Joao Montanari',
            'sexo' : 'masculino',
            'nascimento' : '21/06/2003',
            'telefone' : '(19) 98933-7462'
        }
        return JsonResponse(aluno)
