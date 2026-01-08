pipeline {
    agent any

    environment {
        // Nombre del servicio definido en tu docker-compose.yml
        SERVICE_NAME = 'app-goles'
    }

    stages {
        stage('Checkout') {
            steps {
                // Descarga el código de GitHub
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                echo "Construyendo la imagen de Docker usando Compose..."
                // Construye solo el servicio de la aplicación de Python
                sh "docker compose build ${SERVICE_NAME}"
            }
        }

        stage('Deploy App') {
            steps {
                echo "Desplegando la aplicación..."
                // Levanta el contenedor en segundo plano (-d)
                // --force-recreate asegura que se actualice si cambiaste el código
                sh "docker compose up -d --force-recreate ${SERVICE_NAME}"
            }
        }

        stage('Verify') {
            steps {
                echo "Estado de los contenedores:"
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline finalizado con éxito. La app está corriendo.'
        }
        failure {
            echo '❌ El pipeline falló. Revisa la consola para más detalles.'
        }
    }
}
