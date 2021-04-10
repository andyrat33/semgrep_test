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
docker run -v $(pwd):/src --workdir /src returntocorp/semgrep-agent:v1 python -m semgrep_agent --config p/ci --baseline-ref main
'''
      }
    }

  }
}