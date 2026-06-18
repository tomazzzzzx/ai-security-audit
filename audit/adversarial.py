import torch

def fgsm(model, data, target, eps=0.03):
    data.requires_grad = True
    loss = torch.nn.functional.cross_entropy(model(data), target)
    loss.backward()
    return torch.clamp(data + eps*data.grad.sign(), 0, 1)

def pgd(model, data, target, eps=0.03, alpha=0.01, steps=40):
    adv = data.clone().detach()
    for _ in range(steps):
        adv.requires_grad = True
        loss = torch.nn.functional.cross_entropy(model(adv), target)
        loss.backward()
        adv = torch.clamp(data+torch.clamp(adv+alpha*adv.grad.sign()-data,-eps,eps),0,1).detach()
    return adv
