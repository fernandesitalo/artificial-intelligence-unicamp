class ID:
    def __init__(self, graph, maxDepth):
        self.graph = graph
        self.maxDepth = maxDepth

    def __RevertPath__(self, path):
        list = []
        actualPosition = 'target'
        while actualPosition != 'initial':
            list.append(actualPosition)
            actualPosition = path[actualPosition]
        list.append("initial")
        list.reverse()

        return list
    def run(self):
        stack = [('initial', 0)]
        visitations = 0
        path = {}
        flag = False

        while len(stack) > 0:
            topOfStack = stack.pop()
            depth = topOfStack[1]
            actualPosition = topOfStack[0]

            if depth > self.maxDepth:
                continue

            visitations += 1
            if actualPosition == 'target':
                flag = True
                break

            for child in self.graph[actualPosition]:
                stack.append((child, depth + 1))

                if child not in path:
                    path[child] = actualPosition

        if flag:
            path = self.__RevertPath__(path)
            return (visitations, path)
        else:
            return None