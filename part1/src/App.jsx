import React from 'react';


function App() {
  // Array of image filenames with relative paths
  const relativePath = '../../frameSet/'
  const imageNames = ['2-0.jpg', '2-0.jpg','0-0.jpg']; // Example image path relative to public directory

  return (
    <div>
      <h1>Image Gallery</h1>
      <div className="image-container">
        {imageNames.map((imageName, index) => (
          <img
            key={index}
            src={relativePath+imageName} 
            alt={`Image ${index + 1}`}
            style={{ width: '300px', height: 'auto', marginBottom: '20px' }}
          />
          
        ))}
       
      </div>
    </div>
  );
}

export default App;
