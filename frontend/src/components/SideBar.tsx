import React from "react";

const Sidebar: React.FC = () => {
  return (
    <div className="sidebar">
      <h2>Book History</h2>
      <ul>
        {["Book 1", "Book 2", "Book 3"].map((book, index) => (
          <li key={index}>{book}</li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
