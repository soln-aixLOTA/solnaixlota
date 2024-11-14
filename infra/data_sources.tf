data "aws_eks_cluster" "cluster" {
  name = var.cluster_name
}

data "aws_eks_cluster_auth" "cluster_auth" {
  name = var.cluster_name
} 
terraform { 
  cloud { 
    
    organization = "soln_ai" 

    workspaces { 
      name = "AI" 
    } 
  } 
}