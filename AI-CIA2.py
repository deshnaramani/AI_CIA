# %%
import math

def minimax_alpha_beta(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta, maxDepth):
    # Terminal node (leaf nodes)
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        print(f"Maximizer at depth {depth}, alpha: {alpha}, beta: {beta}")

        # Maximizer's choice (MAX player)
        for i in range(2):
            value = minimax_alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)
            print(f"Maximizer at depth {depth}, updated alpha: {alpha}")

            # Alpha-beta pruning
            if beta <= alpha:
                print(f"Pruning branches at depth {depth}, alpha: {alpha}, beta: {beta}")
                break
        print(f"Maximizer at depth {depth}, selected best: {best}")
        return best
    else:
        best = math.inf
        print(f"Minimizer at depth {depth}, alpha: {alpha}, beta: {beta}")

        # Minimizer's choice (MIN player)
        for i in range(2):
            value = minimax_alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)
            print(f"Minimizer at depth {depth}, updated beta: {beta}")

            # Alpha-beta pruning
            if beta <= alpha:
                print(f"Pruning branches at depth {depth}, alpha: {alpha}, beta: {beta}")
                break
        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best


# Example usage
values = [3, 5, 6, 9, 1, 2, 0, 1]  # Example leaf node values
maxDepth = math.log(len(values), 2)  # Calculate max depth based on the length of values
result = minimax_alpha_beta(0, 0, True, values, -math.inf, math.inf, int(maxDepth))

print(f"Optimal value: {result}")



# %%
