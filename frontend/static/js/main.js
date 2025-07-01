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
