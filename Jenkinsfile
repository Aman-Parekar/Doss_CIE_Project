pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                bat 'python --version'
                bat 'python -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Using a virtual environment is cleaner and avoids permission issues
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
                bat 'venv\\Scripts\\python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CampusFix CI pipeline completed.'
        }
        failure {
            echo 'FAILURE: Check the failed stage in Console Output.'
        }
        always {
            echo 'CampusFix pipeline execution finished.'
        }
    }
}