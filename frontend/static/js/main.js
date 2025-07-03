document.getElementById('studentForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        gpa: parseFloat(document.getElementById('gpa').value),
        activities: document.getElementById('activities').value,
        achievements: document.getElementById('achievements').value,
        target_universities: document.getElementById('targetUniversities').value
    };

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        
        const resultDiv = document.getElementById('result');
        const analysisDiv = document.getElementById('analysis');
        const recommendationsDiv = document.getElementById('recommendations');
        
        analysisDiv.innerHTML = `<h2>분석 결과</h2><p>${data.analysis}</p>`;
        recommendationsDiv.innerHTML = `<h2>추천 사항</h2><p>${data.recommendations}</p>`;
        
        resultDiv.style.display = 'block';
    } catch (error) {
        console.error('Error:', error);
        alert('분석 중 오류가 발생했습니다.');
    }
});

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', function() {
    loadDashboardData();
    loadRecentActivities();
    loadTodoList();
    loadApplicationStatus();
});

// 대시보드 데이터 로드
async function loadDashboardData() {
    try {
        const response = await fetch('/api/dashboard');
        const data = await response.json();
        
        document.getElementById('overallGPA').textContent = data.overall_gpa;
        document.getElementById('targetGPA').textContent = data.target_gpa;
    } catch (error) {
        console.error('Error loading dashboard data:', error);
    }
}

// 최근 활동 로드
async function loadRecentActivities() {
    try {
        const response = await fetch('/api/recent-activities');
        const activities = await response.json();
        
        const container = document.getElementById('recentActivities');
        container.innerHTML = activities.map(activity => `
            <div class="timeline-item">
                <h6>${activity.title}</h6>
                <p class="text-muted">${activity.date}</p>
                <p>${activity.description}</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading activities:', error);
    }
}

// 할 일 목록 로드
async function loadTodoList() {
    try {
        const response = await fetch('/api/todos');
        const todos = await response.json();
        
        const container = document.getElementById('todoList');
        container.innerHTML = todos.map(todo => `
            <li class="list-group-item">
                <div class="todo-item">
                    <div>
                        <input type="checkbox" ${todo.completed ? 'checked' : ''} 
                               onchange="updateTodo(${todo.id}, this.checked)">
                        <span class="${todo.completed ? 'text-muted text-decoration-line-through' : ''}">
                            ${todo.title}
                        </span>
                    </div>
                    <small class="text-muted">${todo.due_date}</small>
                </div>
            </li>
        `).join('');
    } catch (error) {
        console.error('Error loading todo list:', error);
    }
}

// 대학 지원 현황 로드
async function loadApplicationStatus() {
    try {
        const response = await fetch('/api/application-status');
        const status = await response.json();
        
        const container = document.getElementById('applicationStatus');
        container.innerHTML = `
            <div class="mb-3">
                <h6>지원 대학</h6>
                <div class="progress">
                    <div class="progress-bar" role="progressbar" 
                         style="width: ${status.progress}%">
                        ${status.progress}%
                    </div>
                </div>
            </div>
            <div class="small">
                <div>지원 완료: ${status.completed}</div>
                <div>지원 예정: ${status.planned}</div>
                <div>관심 대학: ${status.interested}</div>
            </div>
        `;
    } catch (error) {
        console.error('Error loading application status:', error);
    }
}

// 할 일 상태 업데이트
async function updateTodo(id, completed) {
    try {
        await fetch(`/api/todos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ completed })
        });
        loadTodoList(); // 목록 새로고침
    } catch (error) {
        console.error('Error updating todo:', error);
    }
}
