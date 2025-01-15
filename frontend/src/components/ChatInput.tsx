import React from "react";

const ChatInput: React.FC = () => {
  return (
    <div className="chat-input">
      <input type="text" placeholder="Type your input here..." />
      <button>Send</button>
    </div>
  );
};

export default ChatInput;
