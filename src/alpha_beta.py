
from dataclasses import dataclass
from src.game_tree import GameTree
from src.minimax import is_leaf

@dataclass
class AlphaBetaResult:
    value: int
    nodes_evaluated: int
    branches_pruned: int

def alpha_beta(
    node: GameTree,
    alpha: float = float("-inf"),
    beta: float = float("inf"),
    maximizing_player: bool = True,
) -> AlphaBetaResult:
    if is_leaf(node):
        return AlphaBetaResult(value=node, nodes_evaluated=1, branches_pruned=0)
    
    nodes_evaluated = 0
    branches_pruned = 0
    
    if maximizing_player:
        value = float("-inf")
        for index, child in enumerate(node):
            result = alpha_beta(child, alpha, beta, False)
            nodes_evaluated += result.nodes_evaluated
            branches_pruned += result.branches_pruned
            value = max(value, result.value)
            alpha = max(alpha, value)
            
            if beta <= alpha:
                branches_pruned += len(node) - index - 1
                break
        
        return AlphaBetaResult(int(value), nodes_evaluated, branches_pruned)
    
    value = float("inf")
    for index, child in enumerate(node):
        result = alpha_beta(child, alpha, beta, True)
        nodes_evaluated += result.nodes_evaluated
        branches_pruned += result.branches_pruned
        value = min(value, result.value)
        beta = min(beta, value)
        
        if beta <= alpha:
            branches_pruned += len(node) - index - 1
            break
    
    return AlphaBetaResult(int(value), nodes_evaluated, branches_pruned)
