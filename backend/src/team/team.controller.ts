// team.controller.ts
import { Body, Controller, Delete, Get, Param, Patch, Post, UploadedFile, UseInterceptors } from '@nestjs/common';
import { TeamService } from './team.service';
import { diskStorage } from 'multer';
import { extname } from 'path';
import { FileInterceptor } from '@nestjs/platform-express';
import { teamStorage } from 'src/utils/multer-storage';
import { Team } from './team.entity';

@Controller('team')
export class TeamController {
    constructor(
        private readonly teamService: TeamService) { }

    @Get()
    findAll() {
        return this.teamService.findAll();
    }

    @Post()
    @UseInterceptors(FileInterceptor('photo', { storage: teamStorage }))
    create(@Body() body: any, @UploadedFile() file: Express.Multer.File) {
        return this.teamService.create(body, file?.filename);
    }

    @Patch(':id')
    updateTeam(@Param('id') id: string, @Body() body: Partial<Team>) {
        return this.teamService.updateTeam(+id, body);
    }


    @Patch(':id/photo')
    @UseInterceptors(FileInterceptor('photo', { storage: teamStorage }))
    updatePhoto(@Param('id') id: string, @UploadedFile() file: Express.Multer.File) {
        return this.teamService.updatePhoto(+id, file.filename);
    }

    @Delete(':id')
    deleteTeam(@Param('id') id: string) {
        return this.teamService.deleteTeam(+id);
    }


}




