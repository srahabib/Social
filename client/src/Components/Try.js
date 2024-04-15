import React, { useState } from 'react';

function Try() {
  const [text, setText] = useState('');
  const [scores, setScores] = useState(null);

  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  const analyzeText = () => {
    fetch('/analyze_text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: text }),
    })
      .then((response) => response.json())
      .then((data) => {
        setScores(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div className="container mx-auto py-8">
        
      <div className="max-w-lg mx-auto">
      <h1 className='font-black p-2 text-blue-500'> Try our code and experience the magic behind the scenes ! 🧙‍♂️</h1>
        <div className="mb-4">
          <textarea
            value={text}
            onChange={handleTextChange}
            placeholder="Enter text, e.g., 'I love crypto...'."
            rows={4}
            cols={50}
            className="w-full p-4 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
          />
        </div>
        <div className="mb-4">
          <button
            onClick={analyzeText}
            className="px-6 py-3 bg-blue-500 text-white rounded-md transition duration-300 ease-in-out hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Analyze Text
          </button>
        </div>
        {scores && (
          <div className="border border-gray-300 rounded-md p-4">
            <h2 className="text-xl font-semibold mb-2 text-yellow-500">Analysis Results</h2>
            <p className="mb-2">
              Polarity: <span className="font-semibold text-blue-500">{scores.polarity}</span>
            </p>
            <p className="mb-2">
              Subjectivity: <span className="font-semibold text-blue-500">{scores.subjectivity}</span>
            </p>
            <p className="mb-2">
              Sentiment: <span className="font-semibold text-blue-500">{scores.sentiment}</span>
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Try;
