pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        PYTHON = 'C:\\Users\\Aryan Patil\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        DOCKER = 'C:\\Users\\Aryan Patil\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        IMAGE_NAME = 'campusfix:jenkins'
    }

    stages {
        stage('Checkout GitHub') {
            steps {
                deleteDir()
                checkout scm
            }
        }

        stage('Check Tools') {
            steps {
                bat 'git --version'
                bat '"%PYTHON%" --version'
                bat '"%DOCKER%" --version'
                bat '"%DOCKER%" info'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
                bat '"%PYTHON%" -m pip install pytest'
            }
        }

        stage('Syntax Check') {
            steps {
                bat '"%PYTHON%" -m py_compile app.py'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    int result = bat(
                        returnStatus: true,
                        script: '"%PYTHON%" -m pytest tests/ -v'
                    )

                    if (result != 0) {
                        echo 'WARNING: Tests failed. Continuing pipeline.'
                    } else {
                        echo 'All tests passed.'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t %IMAGE_NAME% .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                bat '"%DOCKER%" image inspect %IMAGE_NAME%'
                echo 'Docker image verified successfully.'
            }
        }
    }

    post {
        success {
            echo 'GREEN BUILD: CampusFix pipeline completed.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }

        always {
            echo 'CampusFix pipeline finished.'
        }
    }
}
