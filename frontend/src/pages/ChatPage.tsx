import React from "react";
import Sidebar from "../components/SideBar";
import Topbar from "../components/Topbar";
import ChatInput from "../components/ChatInput";
import MainArea from "../components/MainArea";

const ChatPage: React.FC = () => {
  return (
    <div className="h-screen flex flex-col">
      <Topbar />
      <div className="flex flex-grow">
        <Sidebar />
        <MainArea />
      </div>
      <ChatInput />
    </div>
  );
};

export default ChatPage;
