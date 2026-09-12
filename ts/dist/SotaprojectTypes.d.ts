export interface Publication {
    author?: string;
    category?: string;
    content?: string;
    id?: string;
    media?: any[];
    published_at?: string;
    title?: string;
    url?: string;
}
export interface PublicationListMatch {
    limit?: number;
    offset?: number;
}
