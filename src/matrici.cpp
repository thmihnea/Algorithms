#include <fstream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

static ifstream cin("matrice.in");
static ofstream cout("matrice.out");

static vector<vector<int>> mat = {};
static vector<int> good_elements = {};

static int n;

struct point {
    int x;
    int y;
};

static void display_matrix(vector<vector<int>> m) {
    for (int i = 0; i < m.size(); i++, cout << endl) {
        for (int j = 0; j < m[0].size(); j++)
            cout << m[i][j] << " ";
    }
}

static void display_vector(const vector<int>& v) {
    for (int i : v)
        cout << i << " ";
}

static vector<int> get_vector_from_matrix(vector<vector<int>> m) {
    vector<int> v = {};
    for (int i = 0; i < m.size(); i++)
        for (int j = 0; j < m[0].size(); j++)
            v.push_back(m[i][j]);
    return v;
}

static bool matrix_contains(vector<vector<int>> m, int element) {
    vector<int> vectorized_matrix = get_vector_from_matrix(std::move(m));
    for (int i : vectorized_matrix)
        if (i == element) return true;
    return false;
}

static int matrix_count_element(vector<vector<int>> m, int element) {
    int counter = 0;
    vector<int> vectorized_matrix = get_vector_from_matrix(std::move(m));
    for (int i : vectorized_matrix) {
        if (i == element) counter++;
    }
    return counter;
}

static bool vector_contains_element(const vector<int>& v, int element) {
    for (int i : v) {
        if (i == element) return true;
    }
    return false;
}

static vector<int> get_corners(vector<vector<int>> m) {
    int size_column = m.size();
    int size_row = m[0].size();
    vector<int> v;
    v.push_back(m[0][0]);
    v.push_back(m[0][size_row - 1]);
    v.push_back(m[size_column - 1][0]);
    v.push_back(m[size_column - 1][size_row - 1]);
    return v;
}

static bool has_one_corner_equal(vector<vector<int>> m1, vector<vector<int>> m2) {
    vector<int> corners_1 = get_corners(std::move(m1));
    vector<int> corners_2 = get_corners(std::move(m2));
    sort(corners_1.begin(), corners_1.end());
    sort(corners_2.begin(), corners_2.end());

    vector<int> intersection = {};
    set_intersection(corners_1.begin(), corners_1.end(),
                     corners_2.begin(), corners_2.end(), back_inserter(intersection));

    return !intersection.empty();
}

static bool in_matrix(vector<vector<int>> m, point p) {
    int size_columns = m.size();
    int size_rows = m[0].size();
    return p.x >= 0 && p.y >= 0 && p.x <= size_columns - 1 && p.y <= size_rows - 1;
}

static int get_matrix_sum(vector<vector<int>> m) {
    int sum = 0;
    for (int i = 0; i < m.size(); i++)
        for (int j = 0; j < m[0].size(); j++)
            sum += m[i][j];
    return sum;
}

static vector<vector<int>> get_sub_matrix(vector<vector<int>> parent_matrix, point start, point end) {
    vector<vector<int>> res = {};

    int i_min = min(start.x, end.x);
    int i_max = max(start.x, end.x);
    int j_min = min(start.y, end.y);
    int j_max = max(start.y, end.y);

    int count = 0;
    for (int i = i_min; i <= i_max; i++) {
        vector<int> v;
        res.push_back(v);
        for (int j = j_min; j <= j_max; j++) {
            int x = parent_matrix[i][j];
            res[count].push_back(x);
        }
        count++;
    }
    return res;
}

static vector<point> get_all_point_permutations(point start, int to_add) {
    point p1 = {start.x + to_add, start.y + to_add};
    point p2 = {start.x + to_add, start.y - to_add};
    point p3 = {start.x - to_add, start.y + to_add};
    point p4 = {start.x - to_add, start.y - to_add};
    vector<point> points = {p1, p2, p3, p4};
    return points;
}

static void compute_property(point p) {
    for (int i = 0; i < n; i++) {
        vector<point> points = get_all_point_permutations(p, i);
        //if (!(in_matrix(mat, points[0])) && !(in_matrix(mat, points[1])) &&
          //  !(in_matrix(mat, points[2])) && !(in_matrix(mat, points[3]))) break;
        for (point new_point : points) {
            if (!(in_matrix(mat, new_point))) continue;
            vector<vector<int>> matrix = get_sub_matrix(mat, p, new_point);
            if (!(has_one_corner_equal(matrix, mat))) continue;
            int sum = get_matrix_sum(matrix);
            if (!(matrix_contains(mat, sum))) continue;
            if (!(vector_contains_element(good_elements, sum)))
                good_elements.push_back(sum);
        }
    }
}

static int compute_final_answer() {
    int counter = 0;
    for (int i = 0; i < good_elements.size(); i++) {
        int appearances = matrix_count_element(mat, good_elements[i]);
        counter += appearances;
    }
    return counter;
}

static void compute_matrix(vector<vector<int>> m) {
    for (int i = 0; i < m.size(); i++)
        for (int j = 0; j < m[0].size(); j++)
            compute_property(point{i, j});
}

int main(int argc, char* argv[]) {
    cin >> n;
    for (int i = 0; i < n; i++) {
        vector<int> v;
        mat.push_back(v);
        for (int j = 0; j < n; j++) {
            int x; cin >> x;
            mat[i].push_back(x);
        }
    }
    compute_matrix(mat);
    cout << compute_final_answer();
}
