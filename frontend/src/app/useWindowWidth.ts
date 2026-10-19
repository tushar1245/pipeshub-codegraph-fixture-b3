import { useEffect, useState } from "react";
import { debounce } from "../lib/debounce";

export function useWindowWidth(): number {
  const [width, setWidth] = useState(() => window.innerWidth);
  useEffect(() => {
    const onResize = debounce(() => setWidth(window.innerWidth), 100);
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);
  return width;
}
