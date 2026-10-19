package errors

import "fmt"

type fundamental struct {
	msg string
}

func New(message string) error {
	return &fundamental{msg: message}
}

func (f *fundamental) Error() string {
	return f.msg
}

func Wrap(err error, message string) error {
	if err == nil {
		return nil
	}
	return fmt.Errorf("%s: %w", message, err)
}
