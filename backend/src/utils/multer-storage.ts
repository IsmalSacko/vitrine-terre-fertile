import { diskStorage } from 'multer';
import { extname } from 'path';

export const teamStorage = diskStorage({
    destination: './uploads/team',
    filename: (_, file, cb) => cb(null, Date.now() + extname(file.originalname)),
});
