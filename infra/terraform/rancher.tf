provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "rancher" {
  name       = "rancher"
  repository = "https://releases.rancher.com/server-charts/stable"
  chart      = "rancher"
  version    = "2.6.3"

  namespace = "cattle-system"

  values = [
    <<EOF
hostname: rancher.yourdomain.com

ingress:
  tls:
    source: secret

replicas: 3

persistence:
  enabled: true
  size: 20Gi
EOF
  ]

  set {
    name  = "bootstrapPassword"
    value = "adminpassword"
  }
} 