import type { ReactNode } from "react";
import { Button } from "./Button";

export interface ModalProps {
  open: boolean;
  title: string;
  onClose: () => void;
  children: ReactNode;
}

export function Modal({ open, title, onClose, children }: ModalProps) {
  if (!open) {
    return null;
  }
  return (
    <div className="modal" role="dialog" aria-label={title}>
      <header>
        <h2>{title}</h2>
        <Button variant="ghost" onClick={onClose}>
          Close
        </Button>
      </header>
      <div className="modal-body">{children}</div>
    </div>
  );
}
