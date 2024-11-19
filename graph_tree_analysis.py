from collections import deque  # ייבוא המחלקה deque לניהול תור עבור BFS

def bfs(adj_matrix, start):
    n = len(adj_matrix)  # מספר הקודקודים בגרף
    visited = [False] * n  # רשימה לסימון קודקודים שביקרנו בהם, בהתחלה כמובן מניחים שלא ביקרנו באף קודקוד
    distance = [0] * n  # רשימה של מרחקים, אתחול המרחקים של כל הקודקודים ל-0
    queue = deque([start])  # יצירת תור שמתחיל עם הקודקוד ההתחלתי
    visited[start] = True  # סימון הקודקוד ההתחלתי כ"visited"
    f_node = start  # אתחול הקודקוד הרחוק ביותר כקודקוד נוכחי
    max_distance = 0  # אתחול המרחק המקסימלי ל-0

    while queue:  # לולאה שרצה כל עוד יש קודקודים בתור
        node = queue.popleft()  # הסרת הקודקוד הראשון מהתור לעיבוד
        for neighbor, connected in enumerate(adj_matrix[node]):  # מעבר על כל השכנים של הקודקוד הנוכחי
            if connected and not visited[neighbor]:  # אם יש קשת לשכן ולא ביקרנו בו עדיין
                visited[neighbor] = True  # סימון השכן כ"visited"
                distance[neighbor] = distance[node] + 1  # חישוב המרחק לשכן + 1
                queue.append(neighbor)  # הוספת השכן לתור לעיבוד נוסף
                if distance[neighbor] > max_distance:  # בדיקה האם המרחק לשכן גדול מהמרחק המקסימלי הנוכחי
                    max_distance = distance[neighbor]  # במידת הצורך, עדכון המרחק המקסימלי
                    f_node = neighbor  # עדכון הקודקוד הרחוק ביותר שנמצא
    return f_node, max_distance, distance  # החזרת הקודקוד הרחוק ביותר, המרחק המקסימלי ורשימת מרחקים


def dfs(v, adj_matrix, visited, parent):
    visited[v] = True  # סימון הקודקוד הנוכחי כ"visited"
    for neighbor, connected in enumerate(adj_matrix[v]):  # מעבר על כל השכנים של הקודקוד הנוכחי
        if connected:  # אם יש קשת לשכן
            if not visited[neighbor]:  # אם לא ביקרנו בשכן עדיין
                if not dfs(neighbor, adj_matrix, visited, v):  # קריאה רקורסיבית ל-DFS עבור השכן
                    return False  # אם מצאנו מעגל, מחזירים False
            elif neighbor != parent:  # אם ביקרנו כבר בשכן והוא לא ההורה של הקודקוד הנוכחי, זהו מעגל
                return False
    return True  # אם לא מצאנו מעגל, נחזיר True


def is_tree(adj_matrix):
    n = len(adj_matrix)  # מספר הקודקודים בגרף
    visited = [False] * n  # רשימה לסימון קודקודים שביקרנו בהם, בהתחלה כמובן מניחים שלא ביקרנו באף קודקוד

    if not dfs(0, adj_matrix, visited, -1):  # התחלת ה-DFS מהקודקוד הראשון (0). אם מצאנו מעגל, נחזיר False
        return False

    if not all(visited):  # אם יש קודקודים שלא ביקרנו בהם, הגרף לא קשיר ולכן לא עץ
        return False

    return True  # אם הגרף קשיר וללא מעגלים, נחזיר True


def tree_attributes(adj_matrix):
    n = len(adj_matrix)  # מספר הקודקודים בגרף

    # נבדוק תחילה אם הגרף הוא עץ
    if not is_tree(adj_matrix):
        return "This graph isn't tree"  # הפונקציה מחזירה הודעת שגיאה אם הגרף אינו עץ

    start_node = 0  # קביעת הקודקוד ההתחלתי כ-0 (קודקוד ראשון)
    f_node, _, _ = bfs(adj_matrix, start_node)  # חיפוש הקודקוד הרחוק ביותר מהקודקוד ההתחלתי
    opposite_node, diameter, dist_from_opposite = bfs(adj_matrix, f_node)  # חיפוש הקודקוד הרחוק ביותר מהקודקוד הרחוק ביותר שנמצא קודם, וחישוב הקוטר

    eccentricities = [0] * n  # רשימה לשמירת האקסצנטריות של כל קודקוד

    # מציאת אקסצנטריות של כל קודקוד בעץ
    for i in range(n):
        _, _, distances = bfs(adj_matrix, i)  # חישוב המרחקים מכל קודקוד אחר
        eccentricities[i] = max(distances)  # אקסצנטריות היא המרחק הגדול ביותר

    radius = min(eccentricities)  # הרדיוס הוא האקסצנטריות הקטנה ביותר
    centers = [i for i in range(n) if eccentricities[i] == radius]  # מציאת הקודקודים שהם מרכזי העץ (בעלי האקסצנטריות הקטנה ביותר)

    return [sorted(centers), int(radius), int(diameter)]  # החזרת המרכזים, הרדיוס, והקוטר של העץ


def is_forest(adj_matrix):
    n = len(adj_matrix)  # מספר הקודקודים בגרף
    visited = [False] * n  # רשימה לסימון קודקודים שביקרנו בהם, בהתחלה כמובן מניחים שלא ביקרנו באף קודקוד

    # בדיקת כל רכיב קשירות בגרף
    for v in range(n):
        if not visited[v]:  # אם לא ביקרנו בקודקוד עדיין
            if not dfs(v, adj_matrix, visited, -1):  # נבצע DFS מהקודקוד הנוכחי, אם מצאנו מעגל נחזיר False
                return False

    return True  # אם כל רכיב קשירות בגרף הוא עץ, נחזיר True

