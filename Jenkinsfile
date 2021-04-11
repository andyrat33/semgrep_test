pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "Building..."'
      }
    }

    stage('Test') {
      steps {
        sh '''echo "Semgrep Testing..."
        ls -la
        sh 'printenv'
        docker run -v $(pwd):/src --workdir /src returntocorp/semgrep-agent:v1 python -m semgrep_agent --config s/andyrat33:unsafe-crypto

        '''

      }
    }

  }
  environment {
    SEMGREP_COMMIT = '$COMMIT'
  }
}