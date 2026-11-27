import { Page } from "@/components/Page";

export default function NotFound() {
  return (
    <Page title="Nothing here" eyebrow="404">
      <p>
        This page does not exist. Try the <a href="/">home page</a>, the{" "}
        <a href="/research">research</a> or the <a href="/numbers">ledger</a>.
      </p>
    </Page>
  );
}
