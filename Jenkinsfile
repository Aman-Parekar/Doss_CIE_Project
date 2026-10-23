
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code retrieved using Jenkins SCM.'
            }
        }

        stage('Check Python') {
            steps {
                bat 'where python'
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --user -r requirements.txt'
                bat 'python -m pip install --user pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
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
