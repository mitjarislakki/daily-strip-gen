import React, { useState } from 'react';

function App() {
  // Array of image filenames with relative paths
  const relativePath = '/frameSet/';
  // Initialize imageNames as a state variable
  const [imageNames, setImageNames] = useState(['2-0.jpg', '2-0.jpg', '0-0.jpg']);

  // Function to update imageNames
  const updateImageNames = (newImageNames) => {
    newImageNames = ['12-0.jpg', '11-0.jpg', '18-0.jpg']
    // Example: Change imageNames to a new set of image filenames

    setImageNames(newImageNames);
  };

  return (
    <div>
      <h1>Funny comic</h1>
      <button onClick={updateImageNames}>Change Images</button>
      <div className="image-container">
        {imageNames.map((imageName, index) => (
          <img
            key={index}
            src={relativePath + imageName}
            alt={`Image ${index + 1}`}
            style={{ width: '300px', height: 'auto', marginBottom: '20px' }}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
