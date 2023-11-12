# ChatBot_MultiPDF
Ce chatbot permettra de répondre aux questions des utilisateurs en extrayant des informations à partir de plusieurs documents au format PDF.

ChatBot avec multiple PDF
cette applicaton de chatbot pour les PDF multiples, est une soluton innovante qui améliore la capacité de recherche et simplifie le processus d'extracton d'informatons à partr de documents PDF. Il propose une architecture modulaire comprenant une interface utlisateur, une compréhension du langage naturel, un stockage vectoriel, des embeddings, et des modèles de langage de grande taille (LLMs). Le chatbot peut interpréter des requêtes en langage naturel, récupérer efficacement des informatons dans les documents PDF, et maintenir la cohérence contextuelle dans les conversatons.

# L'architecture 

![Design sans titre (1)](https://github.com/msallabdelziz/ChatBot_MultiPDF/assets/103082517/a7220f2c-46d0-4d47-9544-58226be1ac9b)

cette applicaton suit une architecture modulaire qui intègre divers composants pour permetre une récupératon efficace des informatons à partr de documents PDF.
De plus, l’applicaton met en avant l'intégraton de l'API OpenAI pour l'utlisaton de modèles de langage de grande taille (LLMs), qui offre des capacités avancées en génératon et compréhension de texte.

C’est une applicaton Python qui nous permet de discuter avec plusieurs documents PDF. On peut poser des questons sur les PDF en utlisant un langage naturel, et l'applicaton fournira des réponses pertnentes en foncton du contenu des documents. cette applicaton utlise un modèle linguistque pour générer des réponses précises à nos questons. Il faut noter aussi que l'applicaton ne répondra qu'aux questons liées aux PDF chargés.


![Design sans titre (2)](https://github.com/msallabdelziz/ChatBot_MultiPDF/assets/103082517/cf26b1e4-ed3c-487d-adb9-716bcb6f4cc5)

   
# Fonctonnement :
 L'applicaton suit ces étapes pour fournir des réponses aux questons :
1. Chargement des PDF : L'applicaton lit plusieurs documents PDF et extrait leur contenu textuel.
2. Découpage du Texte : Le texte extrait est divisé en petts fragments qui peuvent être traités efficacement.
3. Modèle Linguistque : L'applicaton utlise un modèle linguistque pour générer des représentatons vectorielles (embeddings) des fragments de texte.
4. Correspondance de Similarité : Lorsque vous posez une queston, l'applicaton la compare avec les fragments de texte et identfie les plus similaires du point de vue sémantque.
5. Génératon de Réponse : Les fragments sélectonnés sont transmis au modèle linguistque, qui génère une réponse basée sur le contenu pertnent des PDF.
cette approche permet à l'applicaton de comprendre et de répondre aux questons des utlisateurs en se basant sur le contenu des documents PDF chargés.
